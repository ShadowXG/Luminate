from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # post paths
    path('posts/', views.posts_index, name='index'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('posts/<int:post_id>/like/', views.like_toggle, name='like_toggle'),
    path('posts/<int:post_id>/index_like/', views.toggle_index_like, name='toggle_index_like'),
    # add photo path
    path('posts/<int:post_id>/add_photo/', views.add_photo, name='add_photo'),
    # likes path
    path('likes/', views.liked_posts, name='liked_posts'),
    # replies paths
    path('replies/', views.add_reply, name='add_reply'),
    path('replies/<int:pk>/update/', views.ReplyUpdate.as_view(), name='reply_update'),
    path('replies/<int:pk>/delete/', views.ReplyDelete.as_view(), name='reply_delete'),
    # account path
    path('accounts/signup/', views.signup, name='signup'),
]