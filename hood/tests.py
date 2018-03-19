from django.test import TestCase
from .models import Neighborhood
from django.contrib.auth.models import User

# Create your tests here.
class NeighborhoodTestClass(TestCase):
    #setup method
    def setUp(self):
        #set up user class
        self.new_user = User(username='vic',email='vic@mail.com')
        self.new_user.save()
        #set up neighborhood class
        self.embakasi = Neighborhood(name='pipeline',location='embakasi',occupants_count=12,admin=self.new_user)
        self.embakasi.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighborhood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.embakasi,Neighborhood))