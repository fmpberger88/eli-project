from django.urls import path
from .views import forum_index, forum_category, post_detail, add_post, add_reply

urlpatterns = [
    path('', forum_index, name='forum_index'),
    path('category/<str:category_name>/', forum_category, name='forum_category'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('add_post/', add_post, name='add_post'),
    path('add_reply/<int:post_id>/', add_reply, name='add_reply'),
]
