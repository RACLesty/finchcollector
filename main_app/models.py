from django.db import models

# Create your models here.
class Finch(models.Model):
   breed = models.CharField()
   habitat = models.TextField()
   description = models.TextField()
   population = models.IntegerField()

   def __str__(self):
      return self.breed
