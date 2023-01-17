from django.db import models
from .artist import Artist
from .style import Style

class Artist_Style(models.Model):
  
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  style = models.ForeignKey(Style, on_delete=models.CASCADE)

  def __str__(self):
      return self.name
