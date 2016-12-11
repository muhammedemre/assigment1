from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf


def users_index(request):
    return render(request, "users.html")

def register_index(request):
    return render(request, "register.html")

def login_index(request):
    return render(request, "login.html")

def register_success_index(request):
    return render(request, "register_success.html")

def login_success_index(request):
    return render(request, "login_success.html")

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/users/register_success")
    args = {}
    args.update(csrf(request))
    args["form"] = UserCreationForm()
    print args
    return render_to_response("register.html", args)