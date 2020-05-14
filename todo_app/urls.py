# from django.contrib import admin
from django.urls import path, include, re_path

from todo_app import views

urlpatterns = [
    re_path(r'^$', views.todo_app_index, name='todo_app_index_page'),
    re_path(r'^add/$', views.todo_app_add, name='todo_app_add_page'),
    re_path(r'^(?P<todo_id>\d+)/display/$', views.todo_app_display,
            name='todo_app_display_page'),
    re_path(r'^(?P<todo_id>\d+)/update/$', views.todo_app_update,
            name='todo_app_update_page'),
    re_path(r'^(?P<todo_id>\d+)/delete/$', views.todo_app_delete,
            name='todo_app_delete_page'),
]
