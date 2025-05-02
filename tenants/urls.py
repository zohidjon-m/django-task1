from django.urls import path
from .views import TenantDetailView

urlpatterns = [
     path('api/tenants/<int:pk>/', TenantDetailView.as_view(), name = 'tenant-detail'), 
 ]
 