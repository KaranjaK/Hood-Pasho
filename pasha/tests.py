from django.test import TestCase
from .models import Neighborhood, Resident, Business

# Create your tests here.
# Neighborhood class tests
class NeighborhoodTest(TestCase):

    # Method to setup a neighborhood for testing
    def setUp(self):
        self.neighbor = Neighborhood(23,'Umoja Phase1','Umoja-Nairobi',60)
        self.neighbor.create_neighborhood
    
    # Method to test the instance of the neigborhood created
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbor, Neighborhood))

    # Method to test the creation of a new neighborhood
    def test_create_neighborhood(self):
        self.neighbor.create_neighborhood()
        neighbor = Neighborhood.objects.all()
        self.assertTrue(len(neighbor)>0)