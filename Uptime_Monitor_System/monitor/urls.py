from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='monitor-home'),
    path('ajax_json/', views.ajax_json, name='monitor-ajax_json'),
    path('ajax_create/', views.ajax_create, name='monitor-ajax_create'),
    path('ajax_edit/', views.ajax_edit, name='monitor-ajax_edit'),
    path('ajax_delete/', views.ajax_delete, name='monitor-ajax_delete'),

]