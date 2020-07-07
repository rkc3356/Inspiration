from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        #'posts' : Post.objects.all()
    }
    return render(request, 'Inspiration/home.html', context)
