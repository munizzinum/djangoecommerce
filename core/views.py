from django.shortcuts import render
from django.http import HttpResponse


# render search the index.html file in all registered directories.
# They are registered in APP_DIRS, DIRS and for the last one in INSTALLED_APPS.
# This search is by ascending order.
def index(request):
    texts = ['lorem ipsum dolor si amet', 'consectetur adipisicing elit']
    context = {
        'title':'django e-commerce',
        'texts':texts

    }
    return render(request, 'index.html', context)
