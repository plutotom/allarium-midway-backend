from django.contrib.auth.models import User, Group
from rest_framework import serializers
from survey.models import Tenant, Survey, SurveyResponse


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = [
            'id',
            'name',
            'active',
            'context_path',
            'created_by'
        ]        

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = [
            'title',
            'tenant',
            'created_by',
            'active',
            'end_time',
            'data',
        ]


class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = [
            'survey',
            'data',
            'filled_by',
        ]