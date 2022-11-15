from django.urls import path

from .views import PostDetail, PostList, UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>', UserDetail.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('posts/', PostList.as_view()),
]