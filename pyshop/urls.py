"""pyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pages.views import *
from products.views import *
from blog.views import blog_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('contacts/', contact_view),
    path('products/<int:my_id>/', dynamic_lookup_view),
    path('products/', products_page),
    path('blog/', blog_view),
    path('add-product/', products_create_page)
    ]