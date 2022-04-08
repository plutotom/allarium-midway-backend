from unicodedata import name
from survey.models import Tenant, Survey, SurveyResponse
from django.contrib.auth.models import User

admin = User.objects.create(username="admin", email = "admin@example.com", password="admin", is_active=True, is_staff=True, is_superuser =True)
admin.set_password("admin")
admin.save()

tony = User.objects.create(username="tony", email = "tony@example.com", password="secret@123", is_active=True, is_staff=True)
tony.set_password("secret@123")
tony.save()


peter = User.objects.create(username="peter", email = "peter@example.com", password="secret@123", is_active=True, is_staff=True)
peter.set_password("secret@123")
peter.save()

steve = User.objects.create(username="steve", email = "steve@example.com", password="secret@123", is_active=True, is_staff=True)
steve.set_password("secret@123")
steve.save()

tonyCompany = Tenant.objects.create(name= "tony company", active=True, context_path="tony-corp", created_by= tony)
peterCompany = Tenant.objects.create(name= "peter company", active=True, context_path="pert-corp", created_by= peter)
steveCompany = Tenant.objects.create(name= "steve company", active=True, context_path="steve-industries", created_by= steve)


