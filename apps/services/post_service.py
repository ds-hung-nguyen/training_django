from django.urls import reverse
from .service import Service
from apps.models.post import Post
from .user_service import UserService
from apps.support.array_helper import ArrayHelper
from apps.support.datatables import Datatables
from apps.support.helper import constants


class PostService(Service):
    def approved_list(self, params):
        page = int(ArrayHelper.get(params, 'page', 0))
        from_item = page * constants('PAGE_SIZE_DEFAULT')
        to_item = from_item + constants('PAGE_SIZE_DEFAULT')
        return list(Post.objects.order_by('-created_at').filter(approved=True)[from_item:to_item].values('title', 'body', 'author__username', 'created_at'))

    def search(self, params):
        builder = Post.objects.filter(**self.prepare_data_before_search(params))
        return Datatables().query_set(builder)\
            .set_paging_filters(params)\
            .selected_fields(['id', 'title', 'approved', 'author__username']) \
            .set_columns('edit_link', lambda item: reverse('posts.edit', args=[item['id']])) \
            .set_columns('delete_link', lambda item: reverse('posts.delete', args=[item['id']])) \
            .set_columns('approved_link', lambda item: reverse('posts.approved', args=[item['id']]) if 'approved' in item and not item['approved'] else '') \
            .to_array()

    def prepare_data_before_search(self, params):
        filters = {}
        author = ArrayHelper.get(params, 'author', '')
        if author:
            filters['author'] = author
        title = ArrayHelper.get(params, 'title', '')
        if title:
            filters['title__contains'] = title
        return filters

    def get_by_id(self, post_id):
        return Post.objects.get(pk=post_id)

    def create(self, inputs):
        return Post.objects.create(**self.prepare_data_before_create(inputs))

    def prepare_data_before_create(self, inputs):
        user_service = UserService()
        return {
            'title': ArrayHelper.get(inputs, 'title', ''),
            'body': ArrayHelper.get(inputs, 'body', ''),
            'author': user_service.get_by_id(ArrayHelper.get(inputs, 'author', 0)),
        }

    def update(self, post_id, inputs):
        post = self.get_by_id(post_id)
        post.title = ArrayHelper.get(inputs, 'title', '')
        post.body = ArrayHelper.get(inputs, 'body', '')
        return post.save()

    def delete(self, post_id):
        post = self.get_by_id(post_id)
        return post.delete()

    def approved(self, post_id):
        post = self.get_by_id(post_id)
        post.approved = True
        return post.save()
