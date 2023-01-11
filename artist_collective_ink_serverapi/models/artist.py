from django.db import models

class Artist(models.Model):
  
  name = models.CharField(max_length=50)
  instagram = models.CharField(max_length=50)
  artworkPhoto = models.URLField
  # shopId = 
  # styleId = 
  id = models.CharField(max_length=50)
  uid = models.CharField(max_length=50)

def __str__(self):
    return self.name
