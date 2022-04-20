from django.contrib import admin
from .models import Neighborhood, Resident, Business

# Register your models here.
admin.site.register(Neighborhood)
admin.site.register(Resident)
admin.site.register(Business)