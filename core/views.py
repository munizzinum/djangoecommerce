from django.shortcuts import render
from django.http import HttpResponse


# render search the index.html file in all registered directories.
# They are registered in APP_DIRS, DIRS and for the last one in INSTALLED_APPS.
# This search is by ascending order.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def product_list(request):
    return render(request, 'product_list.html')

def product(request):
    return render(request, 'product.html')