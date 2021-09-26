from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='monitor-home'),
    path('', views.home_add, name='monitor-home-add'),
    path('<int:pk>/', views.home_edit, name='monitor-home-edit'),
    path('delete/<int:pk>/', views.home_delete, name='monitor-home-delete'),
    path('ajax_json/', views.ajax_json, name='monitor-ajax_json'),
    path('ajax_create/', views.ajax_create, name='monitor-ajax_create'),


    # path('ajax_home/', views.ajax_home, name='monitor-ajax_home'),
    # path('ajax_get/', views.ajax_get, name='monitor-ajax_get'),
    # path('ajax_home/ajax_create/', views.ajax_create, name='monitor-ajax_create'),
]