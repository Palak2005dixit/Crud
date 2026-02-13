from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register_view, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_task, name='create'),
    path('edit/<int:pk>/', views.edit_task, name='edit'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
]
