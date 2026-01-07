from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_view, name='about'),
    path('books/', views.books_list, name='books_list'),
    path('lessons/', views.lessons_list, name='lessons_list'),
]
