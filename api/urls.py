from django.urls import path
from django.views.generic import TemplateView
from . import views
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('openapi/', get_schema_view(title="Midway API", description="API for developers"), name="openapi-schema"),
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),

    
    path('tenant/<int:pk>/', views.TenantApiView.as_view(), name='api-tenant-read-update-delete'),
    path('tenant/', views.TenantListAPIView.as_view(), name='api-tenant-list-create'),

    path('survey/<int:pk>/', views.SurveyApiView.as_view(), name='api-survey-read-update-delete'),
    path('survey/', views.SurveyListAPIView.as_view(), name='api-survey-list-create'),

    path('survey-response/<int:pk>/', views.SurveyResponseApiView.as_view(), name='api-survey-read-update-delete'),
    path('survey-response/', views.SurveyResponseListAPIView.as_view(), name='api-survey-list-create'),

]





    