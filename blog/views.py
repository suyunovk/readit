from django.shortcuts import render, get_object_or_404, redirect

import contact.models
from .models import (Post, Comment, Tag, Category, HappyClients, About)
from .form import CommentForm

def home_page(request):
    posts = Post.objects.all().order_by('-id')[:6]
    context = {'posts': posts}
    return render(request, "index.html", context)

def about_page(request):
    happy_clients = HappyClients.objects.all()[:3]
    about = About.objects.all()[:1]
    context = {'happy_clients': happy_clients, 'about': about}
    return render(request, "about.html", context)

def blog_page(request):
    posts = Post.objects.all().order_by('-id')[:6]
    search = request.GET.get('search')
    tags = request.GET.get('tags')
    categories = request.GET.get('categories')

    if search:
        posts = posts.filter(title__icontains=search)
    if tags:
        posts = posts.filter(tags__name__icontains=tags)
    if categories:
        posts = posts.filter(categories__name__icontains=categories)

    context = {'posts': posts}
    return render(request, "blog.html", context)

def blog_single_page(request, pk):
    form = CommentForm()
    post = get_object_or_404(Post, pk=pk)
    last_2_posts = Post.objects.order_by('-id')[:2]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    comments = Comment.objects.filter(post__id=pk).order_by('-id')
    recent_blog = Post.objects.all().order_by('-id')[:3]

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect(f'/blog/{post.id}#comments')

    context = {'post': post,
               'form': form,
               'last_2_posts': last_2_posts,
               'categories': categories,
               'tags': tags,
               'comments': comments,
               'recent_blog': recent_blog
               }

    return render(request, "blog-single.html", context)