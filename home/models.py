from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=122)
    pass1= models.CharField(max_length=122)
class UserDetails(models.Model):
        fn = models.CharField(max_length=100)
        email = models.CharField(max_length=144)
        desc = models.CharField(max_length=600)
       
            

        