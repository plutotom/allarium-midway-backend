from django.db import models
from django.contrib.auth.models import User


class Tenant(models.Model):
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=False, null=False, blank=False)
    context_path = models.CharField(max_length=20, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True, blank=False, null=False)
    modified_time = models.DateTimeField(auto_now=True, blank=False, null=False)
    
    def __str__(self):
        return "%s " % (self.name)


class Survey(models.Model):
    title = models.CharField(max_length=200)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)  
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now=True, blank=False, null=False)
    modified_time = models.DateTimeField(auto_now=True, blank=False, null=False)
    active = models.BooleanField(default=False, null=False, blank=False)
    end_time = models.DateTimeField(auto_now=False, blank=False, null=False)
    data =  models.TextField()


class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    data =  models.TextField()
    filled_by = models.CharField(max_length=200)
    created_time = models.DateTimeField(auto_now=True, blank=False, null=False)
