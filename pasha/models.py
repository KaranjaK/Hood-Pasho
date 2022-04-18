import email
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

# Create your models here.

# The Neighborhood model
class Neighborhood(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    occupants = models.IntegerField()
    admin = models.ForeignKey('Resident', on_delete=models.CASCADE, related_name='neighbor')
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
    def find_neighborhood(cls, name):
        return cls.objects.filter(name_icontains=name).all()
    
    # Method to update an occupant
    @classmethod
    def update_occupants(cls, occupants):
        cls.objects.filter(occupants=occupants).update(occupants)


# The User class
class Resident(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    prof_pic = CloudinaryField('image', null = True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, blank=True, related_name='profile')
    email = models.CharField(max_length=50)

    # Method to convert to strings
    def __str__(self):
        return f'{self.user.username} resident'

    # Method to create a user
    @receiver(post_save, sender=User)
    def create_resident(sender, instance, created, **kwargs):
        if created:
            Resident.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_resident(sender, instance, **kwargs):
        instance.resident.save()
    
    @receiver(post_delete, sender=User)
    def delete_resident(sender, instance, **kwards):
        instance.resident.delete()

# The Business class
class Business(models.Model):
    name = models.CharField(max_length=40)
    resident = models.ForeignKey(Resident, on_delete=models.SET_NULL, null = True, blank=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null = True, blank=True)
    email = models.CharField(max_length=50)

    # Method to convert to string
    def __str__(self):
        return self
    
    # Method to create a new user
    def create_business(self):
        self.save()
    
    # Method to delete a business
    def delete_business(self):
        self.delete()

    # Method to update a business
    def update_business(self):
        self.update()

    # Method to search a business
    @classmethod
    def business_search(cls, name):
        return cls.objects.filter(name_icontains=name).all()

    # Method to update a business
    @classmethod
    def update_business(cls, name):
        cls.objects.filter(name=name).update()