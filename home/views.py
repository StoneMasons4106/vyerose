from django.shortcuts import render

# Create your views here.

def index(request):
    '''A view to return the index page'''

    page = {
        'page': 'home',
    }
    return render(request, 'home/index.html', page)
