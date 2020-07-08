from django.db import models

# Create your models here.


class Info(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    age = models.IntegerField(unique=False)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=80)

    def __str__(self):
        return self.fname + ' ' + self.lname
