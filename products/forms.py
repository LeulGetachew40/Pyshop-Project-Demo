from django import forms
from .models import products

class RawProductForm(forms.Form):
    prodname = forms.CharField(label='Product Name', required = False, widget= forms.TextInput(attrs={'placeholder':'Enter Product Name Here'}))
    prod_price = forms.DecimalField(label='Product Price', required = True)
    prod_stock= forms.CharField(label='Product in Stock', required = True, widget= forms.NumberInput())
    # prod_img_url=forms.CharField(label='Product Image', widget= forms.TextInput(attrs={'placeholder':'Enter Image URL Here'}))
    prod_producer= forms.CharField(label='Producer', required = True, initial = 'PyShop', widget= forms.TextInput(attrs={'placeholder':'Enter Producer Here'}))

    # class Meta:
    #     model= products
    #     fields=['prodname',
    #         'prod_price',
    #         'prod_stock',
    #         'prod_producer']
    

    def clean_prodname(self, *args, **kwargs):
        product_name= self.cleaned_data.get('prodname')
        if len(product_name) >= 1 and len(product_name) <= 3:
            raise forms.ValidationError('Name is too short')
        elif product_name == '':
            raise forms.ValidationError('Name cannot be empty.')
        else:
            return product_name
    # def clean(self):
    #     clean = super().clean()
    #     prod_price = self.cleaned_data.get('prod_price')
    #     prod_stock = self.cleaned_data.get('prod_stock')
    #     if prod_price == prod_stock:
    #         raise forms.ValidationError('price and stock are the same amount')
    # def clean(self):
    #     cleaned_data= super().clean()
            # We only use this method if two data fields have dependent validation
            # like password and confirm_password or new_password and old_password