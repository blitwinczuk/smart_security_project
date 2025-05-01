from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('team/', views.team, name='team'),
    path('demo/', views.demo, name='demo'),
    path('homeowner/', views.homeowner_dashboard, name='homeowner_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('resolve/<int:alert_id>/', views.resolve_alert, name='resolve_alert'),
    path('admin_update_status/<int:alert_id>/', views.admin_update_status, name='admin_update_status'),
]
