from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'update_waiter_status/(?P<task_id>\d+)/$', views.update_waiter_task, name='update_waiter_task'),
	url(r'^$', views.waiter, name='waiter'),
]