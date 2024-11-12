from django.contrib import admin
from.models import Service,Category

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    # model=Service
    list_display=['id','menu_name','menu_price','menu_image','menu_description']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','category_slug']


admin.site.register(Service,ServiceAdmin)
admin.site.register(Category,CategoryAdmin)

