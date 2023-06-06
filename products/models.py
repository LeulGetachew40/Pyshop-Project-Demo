from django.db import models

# Create your models here.


def str1(self):
      return self.prodname

class products(models.Model):
    prodname= models.CharField(max_length=255)
    prod_price= models.DecimalField(decimal_places=2, max_digits=2000)
    prod_stock= models.IntegerField(blank=True, default=100)
    prod_img_url= models.CharField(max_length=255)
    prod_producer = models.CharField(max_length=255, null=True, default='Pyshop Original')
    featured= models.BooleanField(null= True, default= False)
    prod_description = models.CharField(max_length=10000, default = 'they are nice')
    __str__ = str1


        #The difference between null and blank
        # null is used in the database level
        # blank is used in the form level (kind of the same thing with required in html)

    # returns a string representation of a models.py
