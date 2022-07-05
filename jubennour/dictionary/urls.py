from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_word', views.add_word, name='add_word'),
    path('delete_word', views.delete_word, name='delete_word'),
    path('search_word', views.search_word, name='search_word'),
    path('edit_word', views.edit_word, name='edit_word'),
]
