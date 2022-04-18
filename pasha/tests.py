from django.test import TestCase
from .models import Neighborhood

# Create your tests here.
# Neighborhood class tests
class NeighborhoodTest(TestCase):
    def setUp(self):
        self.neighbor = Neighborhood('Umoja Phase1','Umoja-Nairobi',60)
        self.neighbor.create_neighborhood
    
    # def test_instance(self):
    #     self.assertTrue(isinstance(self.neighbor, Neighborhood))