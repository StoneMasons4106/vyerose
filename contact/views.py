from django.shortcuts import render
from .models import ContactField

# Create your views here.

def contact(request):
    '''A view to return the contact page'''

    contact_fields = ContactField.objects.values()

    context = {
        'page': 'contact',
        'google_maps_link': contact_fields[0]["google_maps_link"],
        'location_street_address': contact_fields[0]["location_street_address"],
        'location_town_state_zip': contact_fields[0]["location_town_state_zip"],
        'email': contact_fields[0]["email"],
        'phone': contact_fields[0]["phone"],
    }
    
    return render(request, 'contact/contact.html', context)