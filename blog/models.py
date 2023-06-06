from django.db import models
import datetime
# Create your models here.

class Blogs(models.Model):
    date=datetime.datetime.now()
    post=models.TextField(max_length=2000)
    author=models.CharField(max_length=255)
    comment=models.TextField(blank=True, max_length=2000)
    likes_counter=models.IntegerField(blank=True)
    dislike_counter=models.IntegerField()

    #we can pass a default value in the parenthesis if a certain data is not entered in the field
        #For Example we can say...
            #author = models.CharField(default='Mr. X')
    #We can also pass a blank and null values to the Text Field
    #CharField requires us to set a max_length
    #DecimalField means a float number that has a limited decimal value (usually useful for price model)