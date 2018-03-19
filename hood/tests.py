from django.test import TestCase
from .models import Neighborhood,MyUser,Business,Post
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

    def test_save_neighborhood(self):
        self.embakasi.save_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood)>0)

    def test_delete_neighborhood(self):
        self.embakasi.save_neighborhood()
        self.embakasi.delete_neighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood)<1)

    def test_find_neighborhood(self,pk):
        self.embakasi.save_neighborhood()
        neighborhood = Neighborhood.find_neighborhood(pk=Neighborhood.pk)
        self.assertEqual(len(neighborhood),1)

class MyUserTestClass(TestCase):
    def setUp(self):
        #set up user class
        self.new_user=User(username="vic",email="vic@mail.com")
        self.new_user.save()
        #set up neighborhood class
        self.embakasi = Neighborhood(name='pipeline',location='embakasi',occupants_count=12,admin=self.new_user)
        self.embakasi.save_neighborhood()
        #set up myuser class
        self.vick = MyUser(name="Victoria M.",id="32908474",user=self.new_user,neighborhood=self.embakasi)
        self.vick.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighborhood.objects.all().delete()
        MyUser.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.vick,MyUser))

    def test_save_user(self):
        self.vick.save_user()
        users = MyUser.objects.all()
        self.assertTrue(len(users)>0)

    def test_delete_user(self):
        self.vick.save_user()
        self.vick.delete_user()
        users = MyUser.objects.all()
        self.assertTrue(len(users)<1)

class BusinessTestClass(TestCase):
    def setUp(self):
        #set up user class
        self.new_user=User(username="vic",email="vic@mail.com")
        self.new_user.save()
        #set up neighborhood class
        self.embakasi = Neighborhood(name='pipeline',location='embakasi',occupants_count=12,admin=self.new_user)
        self.embakasi.save_neighborhood()
        #set up business class
        self.grocery = Business(name='grocery',email='my_grocery@mail.com',user=self.new_user,neighborhood=self.embakasi)
        self.grocery.save()

    def tearDown(self):
        User.objects.all().delete()
        Neighborhood.objects.all().delete()
        Business.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.grocery,Business))

    def test_save_business(self):
        self.grocery.save_business()
        business =  Business.objects.all()
        self.assertTrue(len(business)>0)

    def test_delete_business(self):
        self.grocery.save_business()
        self.grocery.delete_business()
        business =  Business.objects.all()
        self.assertTrue(len(business)<1)

class PostTestClass(TestCase):
    def setUp(self):
        #set up user class
        self.new_user=User(username="vic",email="vic@mail.com")
        self.new_user.save()
        #set up neighborhood class
        self.embakasi = Neighborhood(name='pipeline',location='embakasi',occupants_count=12,admin=self.new_user)
        self.embakasi.save_neighborhood()
        #set up editor class
        self.vick = MyUser(name="Victoria M.",id="32908474",user=self.new_user,neighborhood=self.embakasi)
        self.vick.save_user()
        #set up post class
        self.new_post=Post(post='I am a test post',editor=self.vick)

    def tearDown(self):
        User.objects.all().delete()
        Neighborhood.objects.all().delete()
        MyUser.objects.all().delete()
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def test_save_post(self):
        self.new_post.save_post()
        post =  Post.objects.all()
        self.assertTrue(len(post)>0)

    def test_delete_post(self):
        self.grocery.save_post()
        self.grocery.delete_post()
        post =  Post.objects.all()
        self.assertTrue(len(post)<1)
