from django.shortcuts import render
from .models import TextField

# Create your views here.

def index(request):
    '''A view to return the home page'''

    text_fields = TextField.objects.values()

    context = {
        'page': 'home',
        'about_title': text_fields[0]["about_title"],
        'about_blurb': text_fields[0]["about_blurb"],
    }
    
    return render(request, 'home/index.html', context)


def privacy_policy(request):

    context = {
        'page': 'home',
    }

    return render(request, 'home/privacypolicy.html', context)
    
