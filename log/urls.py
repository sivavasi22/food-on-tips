# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^userdetail$', views.detail, name='detail'),
    url(r'^aboutus$', views.aboutus, name='aboutus'),

]