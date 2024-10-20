"""Defines URL patterns for blogs."""

from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    # ホームページ
    path('', views.index, name='index'),
    # 作成されたすべてのブログを表示するページ
    path('blogs/', views.blogs, name='blogs'),
    # 個別のブログとそのすべての投稿を表示するページ
    path('blog/<int:blog_id>/', views.blog, name='blog'),

    # 新規ブログの作成ページ
    path('new_blog/', views.new_blog, name='new_blog'),
    # 新規投稿の作成ページ
    path('new_post/<int:blog_id>/', views.new_post, name='new_post'),
    # 既存の投稿の編集ページ
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
]