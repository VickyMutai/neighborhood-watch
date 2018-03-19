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
    
    