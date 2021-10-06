from django.db import models

# Create your models here.

class TextField(models.Model):
    
    name = models.CharField(max_length=50, null=True, blank=True)
    about_title = models.CharField(max_length=500, null=True, blank=True)
    about_blurb = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name
    