from django.urls import path
from . import views



app_name = 'Blog'

urlpatterns = [
    path('', views.Blog_list.as_view(), name='blog_list'),
    path('create_blog/', views.CreateBlog.as_view(), name='create_blog'),
    path('blog_details/<slug:slug>', views.blog_details, name='blog_details'),
    path('liked/<pk>/', views.liked, name = 'liked_post'),
    path('unliked/<pk>/', views.unliked, name='unliked_post'),
    path('my-blogs/', views.my_blogs.as_view(), name='my_blogs'),
    path('update_blog/<pk>/', views.update_blog.as_view(), name='update_blog'),

]
