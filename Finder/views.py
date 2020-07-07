from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author' : 'raaviC',
        'title' : 'Post_1',
        'content' : 'First post content',
        'date_posted' : 'July 4, 2020'
    },
    {
        'author' : 'raaviC',
        'title' : 'Post_2',
        'content' : 'Second post content',
        'date_posted' : 'July 5, 2020'
    }
]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'Inspiration/home.html', context)

def about(request):
    return render(request, 'Inspiration/about.html')
