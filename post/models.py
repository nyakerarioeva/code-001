from django.db import models

# Create your models here.

class Catalogue(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return str(self.title)
    
class CustomerEntry(models.Model):
    entry = models.ForeignKey(Catalogue, on_delete=models.CASCADE,related_name="entries" )
