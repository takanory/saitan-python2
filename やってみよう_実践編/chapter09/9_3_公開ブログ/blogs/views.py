from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Blog, BlogPost
from .forms import BlogForm, BlogPostForm


def index(request):
    """ブログのホームページ"""
    return render(request, 'blogs/index.html')

def blogs(request):
    """作成されたすべてのブログを表示するページ"""
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """個別のブログとそのすべての投稿を表示するページ"""
    blog = Blog.objects.get(id=blog_id)
    posts = blog.blogpost_set.all()

    context = {'blog': blog, 'posts': posts}
    return render(request, 'blogs/blog.html', context)

@login_required
def new_blog(request):
    """新規ブログの作成ページ"""
    if request.method != 'POST':
        # データは送信されていないので空のフォームを生成する
        form = BlogForm()
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')

    # 空または無効のフォームを表示する
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

@login_required
def new_post(request, blog_id):
    """新規投稿の作成ページ"""
    blog = Blog.objects.get(id=blog_id)
    check_blog_owner(blog, request.user)

    if request.method != 'POST':
        # データは送信されていないので空のフォームを生成する
        form = BlogPostForm()
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.blog = blog
            new_post.save()
            return redirect('blogs:blog', blog_id=blog_id)

    # 空または無効のフォームを表示する
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, post_id):
    """既存の投稿の編集ページ"""
    post = BlogPost.objects.get(id=post_id)
    blog = post.blog
    check_blog_owner(blog, request.user)

    if request.method != 'POST':
        # 初回リクエスト時は現在の投稿の内容がフォームに埋め込まれている
        form = BlogPostForm(instance=post)
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = BlogPostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blog', blog_id=blog.id)

    context = {'post': post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

def check_blog_owner(blog, user):
    """Make sure the currently logged-in user owns the blog that's 
    being requested.

    Raise Http404 error if the user does not own the blog.
    """
    if blog.owner != user:
        raise Http404