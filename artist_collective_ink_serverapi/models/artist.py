from django.db import models
from .shop import Shop
from .style import Style

class Artist(models.Model):
  
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  instagram = models.CharField(max_length=50)
  artworkPhoto = models.URLField()
  shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
  style = models.ForeignKey(Style, on_delete=models.CASCADE)

def __str__(self):
    return self.name
