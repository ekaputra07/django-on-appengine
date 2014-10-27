from django.shortcuts import render, get_object_or_404
from django.http import Http404

import markdown

from blog.models import Post


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def post(request, post_id, post_slug):
    post = get_object_or_404(Post, pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)
