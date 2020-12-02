from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category


def index(request):
    posts = Post.objects.all()[:5]
    categories = Category.objects.all()
    return render(request, 'index.html', {'posts': posts, 'categories': categories})


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'post.html', {'post': post})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category)
    categories = Category.objects.all()
    return render(request, 'category.html', {'category': category, 'posts': posts, 'categories': categories})


def test_bootstrap(request):
    return render(request, 'test_bootstrap.html')
