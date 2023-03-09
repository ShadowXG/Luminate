from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts_index, name='index'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('posts/<int:post_id>/like/', views.toggle_like, name='toggle_like'),
    path('likes/', views.liked_posts, name='liked_posts'),
    path('replies/', views.add_reply, name='add_reply'),
    path('accounts/signup/', views.signup, name='signup'),
]