from django.db import models

class Movie(models.Model):
   title = models.CharField(max_length=100)
   overview = models.TextField()
   director = models.CharField(max_length=30)
   actor = models.CharField(max_length=100)
   poster = models.ImageField(blank=True) 

   def __str__(self):
       return self.title
