from django.test import TestCase
from django.urls import reverse 
from rest_framework.test import APIClient
from rest_framework import status
from tenants.models import Tenant


class TenantDetailAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.tenant = Tenant.objects.create(
            name="Tenant Test",
            domain="tenant-test.com",
            config_json= {"enable_feature_x": True, "theme":"blue"}
        )
        
    def test_get_existing_tenant(self):
        url = f'/api/tenants/{self.tenant.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.tenant.name)
        self.assertEqual(response.data['domain'], self.tenant.domain)
        self.assertEqual(response.data['config_json']['theme'],"blue")
        
    def test_get_non_existing_tenant(self):
        url = '/api/tenants/999/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        