from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100, unique=True)
    config_json = models.JSONField()
    
    
    def __str__(self):
        return self.name