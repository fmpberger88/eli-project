# forum/urls.py

from django.urls import path
from .views import forum_index, forum_category, post_detail, forum_search, add_post, add_comment, add_reply

urlpatterns = [
    path('', forum_index, name='forum_index'),
    path('category/<str:category_name>/', forum_category, name='forum_category'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('search/', forum_search, name='forum_search'),
    path('add_post/', add_post, name='add_post'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),
    path('add_reply/<int:comment_id>/', add_reply, name='add_reply'),
]
