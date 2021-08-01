from django.urls import path

from .views import post_view, user_view, auth_view, top_view, site_view

urlpatterns = [
    #: Auth
    path('login', auth_view.login, name='auth.login'),
    path('logout', auth_view.logout, name='auth.logout'),
    #: Site
    path('', site_view.index, name='sites.index'),
    #: Top
    path('top', top_view.index, name='top.index'),
    #: Post
    path('posts', post_view.index, name='posts.index'),
    path('posts/<int:post_id>/', post_view.show, name='posts.show'),
    path('posts/create/', post_view.create, name='posts.create'),
    path('posts/<int:post_id>/edit/', post_view.edit, name='posts.edit'),
    path('posts/<int:post_id>/delete/', post_view.delete, name='posts.delete'),
    path('posts/<int:post_id>/approved/', post_view.approved, name='posts.approved'),
    path('posts/search', post_view.search, name='posts.search'),
    path('posts/list', post_view.list, name='posts.list'),
    #: User
    path('users', user_view.index, name='users.index'),
    path('users/<int:user_id>/', user_view.show, name='users.show'),
    path('users/create/', user_view.create, name='users.create'),
    path('users/<int:user_id>/edit/', user_view.edit, name='users.edit'),
    path('users/<int:user_id>/delete/', user_view.delete, name='users.delete'),
    path('users/search', user_view.search, name='users.search')
]
