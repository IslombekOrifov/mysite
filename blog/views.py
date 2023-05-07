import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post, Category


def post_list(request, slug=None):
    category = None
    recently_posts = Post.published.all().select_related('category').order_by('-publish')[:3]

    if slug:
        post_list = Post.published.filter(category__slug=slug).select_related('category')
        category = Category.objects.get(slug=slug)
    else:
        post_list = Post.published.all().select_related('category')
    
    paginator = Paginator(post_list, 9)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {
        'posts': posts, 
        'current_cat': category,
        'recently_posts': recently_posts
    }
    return render(request, 'blog/post/list.html', {'posts': posts, 'current_cat': category})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post, 
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    recently_posts = Post.published.all().order_by('-publish')[:3]
    category = Category.objects.get(id=post.category.id)
    context = {
        'post': post, 
        'current_cat': category,
        'recently_posts': recently_posts
    }
    return render(request, 'blog/post/detail.html', context)
