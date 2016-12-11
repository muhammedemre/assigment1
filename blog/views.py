from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog_List

def indexBlog(request):
    return HttpResponse("<a href='entries'> Click to see a better page  </a>")

def entries(request):
    return render(request, "blog_entries.html", {"Blog_List":Blog_List})

def specificEntry(request, blog_pk):
    try:
        return HttpResponse(Blog_List[int(blog_pk) - 1])
    except IndexError:
        raise Http404("There is nothing to show")


