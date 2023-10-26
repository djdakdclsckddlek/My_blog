from django.shortcuts import render


def posts(request):
    return render(request, 'blog/blogposts.html')
# Create your views here.
