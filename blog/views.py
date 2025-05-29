from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1, is_active=True)
    template_name = "blog/index.html"

def about_us(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/about_us.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/about_us.html",
        {"post": post},
    )