from django.test import TestCase
from .models import Neighborhood, Resident, Business

# Create your tests here.
# Neighborhood class tests
class NeighborhoodTest(TestCase):

    # Setting up a neighborhood for testing
    def setUp(self):
        self.neighbor = Neighborhood('23','Umoja Phase1','Umoja-Nairobi',60)
        self.neighbor.create_neighborhood
    
    # Testing the instance of the neigborhood created
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbor, Neighborhood))

    # Testing the creation of a new neighborhood
    def test_create_neighborhood(self):
        self.neighbor.create_neighborhood()
        neighbor = Neighborhood.objects.all()
        self.assertTrue(len(neighbor)>0)

    # Testing the deleting of a neighborhood
    def test_delete_neighborhood(self):
        self.neighbor.delete_neighborhood()
        neighbor = Neighborhood.objects.all()
        self.assertTrue(len(neighbor)==0)
    
    # Testing the update of a neighborhood
    def test_update_neighborhood(self):
        new_hood = 'Donholm'
        self.neighbor.update_neighborhood(self.neighbor.id, new_hood)
        changed_hood = Neighborhood.objects.filter(id=23).update(name='Donhom')
        self.assertTrue(len(changed_hood) > 0)