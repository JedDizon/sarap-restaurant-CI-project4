from django.shortcuts import render
from .models import About
from blog.models import Post

# def about_me(request):
#     """
#     Renders the About page
#     """
#     about = About.objects.all().order_by('-updated_on').first()

#     return render(
#         request,
#         "about/about.html",
#         {"about": about},
#     )

def about_view(request):
    post = Post.objects.filter(status=1).order_by('-created_on').first()
    return render(
        request,
        'about/about.html',
        {'post': post},
    )