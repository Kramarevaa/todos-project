from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about_index', views.about_index, name='about_index'),
    path('text', views.text, name='text'),
    path('create_task', views.create_task, name='create_task'),
    path('complete_task/<int:task_id>', views.complete_task, name='complete_task'),
    path('delete_task/<int:task_id>', views.delete_task, name='delete_task'),
]