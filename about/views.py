from django.shortcuts import render
from .models import About
from blog.models import Post


def about_view(request):
    posts = Post.objects.filter(status=1, is_active=True).order_by('-created_on')[:3]
    return render(
        request,
        'about/about.html',
        {'posts': posts},
    )