from django.db import models

class Style(models.Model):
  
  name = models.CharField(max_length=50)
  id = models.CharField(max_length=50)
  uid = models.CharField(max_length=50)

  def __str__(self):
      return self.name
