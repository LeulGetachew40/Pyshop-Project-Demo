from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request, *args, **kwargs):
    # return HttpResponse('<h1>HELLO WORLD</h1>')
    # products = models.products.objects.all()
    return render(request, 'home.html', {})

def contact_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Contacts</h1>')
    return render(request, 'contact.html', {})