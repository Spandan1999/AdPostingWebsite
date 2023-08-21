from django.urls import path
from . import views

urlpatterns = [
    path('', views.Homepage, name='Homepage'),
    path('login/', views.loginPage, name='loginPage'),
    path('signup/', views.registerPage, name='registerPage'),
    path('logout/', views.logoutUser, name='logoutUser'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('feed/', views.feed, name='feed'),
    path('ad/<str:pk>/', views.AdPostDetailView, name='ad'),
    path('delete/<str:pk>/', views.delete_post, name='delete_post'),
    path('update/<str:pk>/', views.update_post, name='update_post')
]