from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.users_index),
    url(r'^register/', views.register_user),
    url(r'^register_success/$', views.register_success_index),
    url(r'^login/$', views.login_index),
    url(r'^login_success/$', views.login_success_index),
]