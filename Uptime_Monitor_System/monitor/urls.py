from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='monitor-home'),
    path('', views.home_add, name='monitor-home-add'),
    path('<int:pk>/', views.home_edit, name='monitor-home-edit'),
    path('delete/<int:pk>/', views.home_delete, name='monitor-home-delete'),
]