from django.shortcuts import render
from .models import TextField
from products.models import Category

# Create your views here.

def index(request):
    '''A view to return the home page'''

    text_fields = TextField.objects.values()
    categories = Category.objects.values()

    context = {
        'page': 'home',
        'about_title': text_fields[0]["about_title"],
        'about_blurb': text_fields[0]["about_blurb"],
        'categories': categories,
    }
    
    return render(request, 'home/index.html', context)
