from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Neighborhood(models.Model):
    name =  models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    occupants_count = models.PositiveIntegerField(default=0)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,pk):
        neighborhood=Neighborhood.objects.filter(pk=Neighborhood.pk)
        return neighborhood

    @classmethod
    def update_neighborhood(cls,id,name):
        updated = Neighborhood.objects.filter(id=Neighborhood.id).update(name=name)
        return updated

    @classmethod
    def update_occupants(cls,id,occupants_count):
        occupied = Neighborhood.objects.filter(id=Neighborhood.id).update(occupants_count=occupants_count)
        return occupied

class Business(models.Model):
    name = models.CharField(max_length=60)
    business_email = models.EmailField(max_length=60)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls,search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business

    @classmethod
    def update_business(cls,id,name):
        updated = Business.objects.filter(id=business.id).update(name=name)

class MyUser(models.Model):
    name = models.CharField(max_length=60)
    id_no = models.CharField(max_length=60)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    business = models.ForeignKey(Business,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()