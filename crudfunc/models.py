from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=23)
    description = models.CharField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    