from django.db import models

# Create your models here.

# The Neighborhood model
class Neighborhood(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    occupants = models.IntegerField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

    def __st__(self):
        return self

    def create_neighborhood(self):
        self.save()

    