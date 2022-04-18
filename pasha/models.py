import email
from django.db import models
from unicodedata import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

# The Neighborhood model
class Neighborhood(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    occupants = models.IntegerField()
    admin = models.ForeignKey('Resident', on_delete=models.CASCADE)
    hood_pic = CloudinaryField('image')
    description = models.CharField(max_length=300)
    health_contact = models.IntegerField(null=True, blank=True)
    police_contact = models.IntegerField(null=True, blank=True)

    def __st__(self):
        return self

    def create_neighborhood(self):
        self.save()

# The User class
class Resident(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.CharField(max_length=50)

# The Business class
class Business(models.Model):
    name = models.CharField(max_length=40)
    resident = models.ForeignKey(Resident, on_delete=models.SET_NULL, null = True, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null = True, blank=True)
    email = models.CharField(max_length=50)