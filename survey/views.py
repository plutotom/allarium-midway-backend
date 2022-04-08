from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User, Group

from survey.serializers import GroupSerializer, UserSerializer


# Create your views here.
def index(request):
    return render(request, 'index.html')

def take_survey(request):
    return render(request, 'survey.html')