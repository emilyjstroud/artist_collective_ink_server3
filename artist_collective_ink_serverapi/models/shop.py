from django.db import models

class Shop(models.Model):
  
  name = models.CharField(max_length=50)
  location = models.CharField(max_length=50)
  website = models.URLField()
  photo = models.URLField()
  user = models.CharField(max_length=50)

  def __str__(self):
      return self.name
