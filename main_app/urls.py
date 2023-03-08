from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts_index, name='index'),
    path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
    path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    # like association
    # path('posts/<int:post_id>/assoc_like/<int:like_id/', views.assoc_like, name='assoc_like'),
    # like unassociation
    # path('posts/<int:post_id>/unassoc_like/<int:like_id/', views.unassoc_like, name='unassoc_like'),
    # paths for likes
    path('likes/', views.LikeList.as_view(), name='like_index'),
    path('likes/create/', views.LikeCreate.as_view(), name='likes_create'),
    path('likes/<int:pk>/delete/', views.LikeDelete.as_view(), name='likes_delete'),
]