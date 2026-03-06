from django.db import models

class Post(models.Model):
  title = models.CharField(max_length=200)
  date = models.DateTimeField('data published')
  content = models.TextField()
  
  def __str__(self):
    return self.title