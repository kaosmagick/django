from django.db import models


# Create your models here.
class Contact(models.Model):
    fname=models.CharField(max_length=60)
    lname=models.CharField(max_length=60)
    email=models.CharField(max_length=122)
    phone=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.fname