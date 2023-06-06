from django.shortcuts import render
from django.http import HttpResponse, Http404
from .forms import RawProductForm
from .models import products
from blog.models import Blogs

def products_page (request):
    obj = products.objects.all()
    blog_obj = Blogs.objects.all()
    return render(request, 'products/products_detail.html', {'products': obj, 'blog': blog_obj})

def dynamic_lookup_view (request, my_id):
    try:
        obj = products.objects.get(id=my_id)
    except products.DoesNotExist:
        raise Http404
    return render(request, 'products/products_dynamic_detail.html', {'products': obj})

# def products_create_page(request, *args, **kwargs):
#     form = RawProductForm()
#     if request.method == 'POST':
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             # # RawProductForm.clean_prodname()
#             # products.objects.create(**form.cleaned_data)
#             # form = RawProductForm()
#             form.save()
#         #     form=RawProductForm()
#         # else:
#         #     print(form.errors)
#     # form = RawProductForm()
#     return render(request, 'products/products_create_form.html', {'form': form})
# , *args, **kwargs
def products_create_page(request):
    form = RawProductForm(request.POST or None)
    if form.is_valid(): # is_valid() runs the clean() and clean_<field_name> methods
        # form.save()
        # Only used with forms.ModelForm
        products.objects.create(**form.cleaned_data)
        # Only used with forms.Form
        form = RawProductForm()
    else:
        print(form.errors)
    # form= RawProductForm()
    return render(request, 'products/products_create_form.html', {'form': form})