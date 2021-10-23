from django.db import models

# Create your models here.

class post(models.Model):
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    links = models.CharField(max_length=1000)
    
    def __str__(self):
        return str(self.title)
