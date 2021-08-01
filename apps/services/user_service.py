from django.urls import reverse
from django.contrib.auth.models import User
from .service import Service
from apps.support.array_helper import ArrayHelper
from apps.support.datatables import Datatables
from django.contrib.auth.hashers import make_password


class UserService(Service):
    def list(self):
        return User.objects.all()

    def get_by_id(self, user_id):
        return User.objects.get(pk=user_id)

    def search(self, params):
        builder = User.objects.filter(**self.prepare_data_before_search(params))
        return Datatables().query_set(builder)\
            .set_paging_filters(params)\
            .selected_fields(['id', 'username', 'first_name', 'last_name', 'is_superuser', 'email']) \
            .set_columns('fullname', lambda item: item['last_name'] + item['first_name']) \
            .set_columns('edit_link', lambda item: reverse('users.edit', args=[item['id']])) \
            .set_columns('delete_link', lambda item: reverse('users.delete', args=[item['id']])) \
            .to_array()

    def prepare_data_before_search(self, params):
        filters = {}
        if 'username' in params and params['username']:
            filters['username__contains'] = params['username']
        if 'email' in params and params['email']:
            filters['email__contains'] = params['email']
        return filters

    def create(self, inputs):
        return User.objects.create(**self.prepare_data_before_create(inputs))

    def prepare_data_before_create(self, inputs):
        return {
            'username': ArrayHelper.get(inputs, 'username', ''),
            'password': make_password(ArrayHelper.get(inputs, 'password', '')),
            'first_name': ArrayHelper.get(inputs, 'first_name', ''),
            'last_name': ArrayHelper.get(inputs, 'last_name', ''),
            'email': ArrayHelper.get(inputs, 'email', ''),
            'is_superuser': ArrayHelper.get(inputs, 'is_admin', False),
        }

    def update(self, user_id, inputs):
        user = self.get_by_id(user_id)
        user.first_name = ArrayHelper.get(inputs, 'first_name', '')
        user.last_name = ArrayHelper.get(inputs, 'last_name', '')
        user.email = ArrayHelper.get(inputs, 'email', '')
        user.is_superuser = ArrayHelper.get(inputs, 'is_admin', False)
        return user.save()

    def delete(self, user_id):
        user = self.get_by_id(user_id)
        return user.delete()
