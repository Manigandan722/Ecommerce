from django.db import models
import datetime
import os
# Create your models here.
def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    New_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',New_filename)


class Catagory(models.Model):
    name=models.CharField(max_length=150 ,null= False ,blank=False)
    image=models.ImageField(upload_to=getFileName ,null= True, blank=True )
    Descripion=models.TextField(max_length=500, null= False, blank=False)
    status=models.BooleanField(default=False ,help_text="0-default,1-hidden")
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    Catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name=models.CharField(max_length=150 ,null= False ,blank=False)
    vender=models.CharField(max_length=150 ,null= False ,blank=False)
    product_image=models.ImageField(upload_to=getFileName ,null= True, blank=True )
    quantity=models.IntegerField(null=False,blank=False)
    Original_orice=models.FloatField(null=False,blank=False)
    Selling_price=models.FloatField(null=False,blank=False)
    Descripion=models.TextField(max_length=500, null= False, blank=False)
    status=models.BooleanField(default=False ,help_text="0-default,1-hidden")
    trending=models.BooleanField(default=False ,help_text="0-default,1-")
    created_at=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    