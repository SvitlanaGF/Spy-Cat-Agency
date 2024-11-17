from django.db import models

# Create your models here.
class SpyCat(models.Model):
    name = models.CharField(max_length=100)
    yearsOfExperience = models.IntegerField()
    breed = models.CharField(max_length=100)
    salary = models.IntegerField()
    def __str__(self):
        return self.name
