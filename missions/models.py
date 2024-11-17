from django.db import models
from spy_cat_app.models import SpyCat

class Target(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    notes = models.TextField()
    isComplete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Mission(models.Model):
    name = models.CharField(max_length=100)
    cat = models.ForeignKey(SpyCat, on_delete=models.CASCADE)
    targets = models.ManyToManyField(Target)
    isComplete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
