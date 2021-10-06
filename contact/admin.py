from django.contrib import admin
from .models import ContactField

# Register your models here.

class ContactFieldAdmin(admin.ModelAdmin):
    list_display=(
        'name',
        'location_street_address',
        'location_town_state_zip',
        'email',
        'phone',
    )

    ordering = (
        'name',
    )


admin.site.register(ContactField, ContactFieldAdmin)