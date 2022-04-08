from django.test import TestCase

from survey.models import Survey, Tenant


'''
            Execute it with
            python manage.py test survey
'''
class SurveyModelTests(TestCase):
    def testModel(self):
            
        tenant = Tenant(name = 'company1') 
        tenant.save()

        survey = Survey(title = 'sample survey', tenant = tenant)
        survey.save()

        print("tenant is:", tenant) 

        print(Survey.objects.filter(tenant = tenant))
        print(Survey.objects.filter(tenant__pk = 1))
       
        # python manage.py test survey

