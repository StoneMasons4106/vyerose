from django.shortcuts import render

# Create your views here.

def contact(request):
    '''A view to return the index page'''

    page = {
        'page': 'contact',
    }
    return render(request, 'contact/contact.html', page)