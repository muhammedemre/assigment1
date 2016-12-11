from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexTodo),
    url(r'^(?P<todo_pk>[0-9]+)', views.specificTodo)
]