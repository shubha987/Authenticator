from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    repassword = models.CharField(max_length=100)
    date=models.DateField()

    # Add more fields as needed

    def __str__(self):
        return self.firstname

