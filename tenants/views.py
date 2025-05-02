from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Tenant

class TenantDetailView(APIView):
    
    permission_classes = [AllowAny]
    
    def get(self, request, pk):
        tenant = get_object_or_404(Tenant, pk=pk)
        return Response({
            "id": tenant.id,
            "name": tenant.name,
            "domain": tenant.domain,
            "config_json": tenant.config_json,
        })
        