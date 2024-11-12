from django.db import models
from autoslug import AutoSlugField


# Create a Manager
class ServiceCustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def nicaragua_Whole_Bean(self):
        return super().get_queryset().filter(menu_brand="Nicaragua_Whole_Bean")
    
    def culumbia_Whole_Bean(self):
        return super().get_queryset().filter(menu_brand="Culumbia_Whole_Bean")

    def peru_Whole_Bean(self):
        return super().get_queryset().filter(menu_brand="Peru_Whole_Bean")






# Create your models here.

class Category(models.Model):
    category_name=models.CharField(max_length=100,null=False)
    category_slug=AutoSlugField(populate_from="category_name",unique=True)

    def __str__(self):
        return self.category_name 
    
class Service(models.Model):
    menu_name=models.CharField(max_length=100, null=False)
    menu_price=models.PositiveIntegerField(default=50)
    menu_image=models.ImageField(upload_to="services/")#image folder path
    menu_description=models.TextField(default="add your description here")
    menu_brand=models.CharField(max_length=100,default="coffee")
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

# creat manager
    customManager=ServiceCustomManager()


    def __str__(self):
        return self.menu_name

