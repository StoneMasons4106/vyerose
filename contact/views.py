from django.shortcuts import render, redirect
from .models import ContactField
from products.models import Category
from django.core.mail import EmailMessage
from django.contrib import messages
import os

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


def send_message(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        user_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        to_email = ContactField.objects.values()[0]["email"]

        email = EmailMessage(f'You have a new message from {name}', 
        f'You have a new email from { name }!\n\nEmail: { user_email }\n\nSubject: { subject }\n\nMessage: { message }',
        to=[to_email])
        email.send()
        messages.success(request, 'Your message has been sent!')

        return redirect('contact')