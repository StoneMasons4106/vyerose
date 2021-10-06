from django.db import models

# Create your models here.

class ContactField(models.Model):

    name = models.CharField(max_length=50, null=True, blank=True)
    google_maps_link = models.CharField(max_length=2000, null=True, blank=True)
    location_street_address = models.CharField(max_length=200, null=True, blank=True)
    location_town_state_zip = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)

    def __str__(self):
        return self.name