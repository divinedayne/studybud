from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.LogOut, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('rooms/<str:pk>/', views.room, name='room'),
    path('create-room/', views.createRoom, name='create-room'), 
    path('edit-room/<str:pk>/', views.updateView, name='edit-room'),
    path('delete-room/<str:pk>/', views.deleteView, name='delete-room')


]