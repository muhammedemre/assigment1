from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.indexBlog),
    url(r'^entries/$', views.entries),
    url(r'^entries/(?P<blog_pk>[0-9]+)', views.specificEntry),

]