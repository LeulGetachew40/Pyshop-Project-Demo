from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogs
from products.models import products
# Create your views here.

def blog_view (request, *args, **kwargs):
    thing = Blogs.objects.all()
    farn  = products.objects.all()
    return render(request, 'blogview/detail.html', {'blogs': thing, 'farn': farn})