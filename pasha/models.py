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

    # Method to convert inputs to a string
    def __st__(self):
        return self

    # Method to create a new neighborhood
    def create_neighborhood(self):
        self.save()

    # Method to delete an existing neighborhood
    def delete_neighborhood(self):
        self.delete()
    
    # Method to update a neighborhood
    def update_neighborhood(self):
        self.update()
    

    # Method to search a neighborbood
    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
    
    # Method to update an occupant
    @classmethod
    def update_occupants(cls, occupants):
        cls.objects.filter(occupants=occupants).update(occupants)


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