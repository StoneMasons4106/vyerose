from django.shortcuts import render
from .models import TextField

# Create your views here.

def index(request):
    '''A view to return the home page'''

    text_fields = TextField.objects.values()

    try:
        about_title = text_fields[0]["about_title"]
    except:
        about_title = ""

    try:
        about_blurb = text_fields[0]["about_blurb"]
    except:
        about_blurb = ""

    context = {
        'page': 'home',
        'about_title': about_title,
        'about_blurb': about_blurb,
    }
    
    return render(request, 'home/index.html', context)


def privacy_policy(request):

    context = {
        'page': 'home',
    }

    return render(request, 'home/privacypolicy.html', context)
    
