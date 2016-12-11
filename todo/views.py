from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Todo_List

def indexTodo(request):
    return render(request, "todo.html", {"Todo_List":Todo_List})

def specificTodo(request, todo_pk):
    try:
        return HttpResponse(Todo_List[int(todo_pk)-1])
    except IndexError:
        raise Http404("There is nothing to show")