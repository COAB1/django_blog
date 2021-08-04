from django.shortcuts import render
from .models import Post

posts = [
    {
        'author': 'COAB1',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 2, 2021'
    },
    {
        'author': 'Jne Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 3, 2021'
    }
]

def home (request):
    context = {
        'posts': Post.objects.all() 
    }
    return render(request, 'blog/home.html', context)

def about (request):
    return render(request, 'blog/about.html', {'title': 'About'})