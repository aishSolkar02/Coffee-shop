from django.shortcuts import render
from .models import Service,Category
from django.views.generic import ListView,DetailView



# Create your views here.



def nicaragua_Whole_Bean(request):
    services=Service.customManager.nicaragua_Whole_Bean()

    return render(request,"services.html",{"services":services})

def culumbia_Whole_Bean(request):
    services=Service.customManager.culumbia_Whole_Bean()
    return render(request,"services.html",{"services":services})

def peru_Whole_Bean(request):
    services=Service.customManager.peru_Whole_Bean()
    return render(request,"services.html",{"services":services})


    # ---------------------------------------------------------------------------------------

def search(request):
    keyword=request.GET.get("keyword")
    services=Service.customManager.all().filter(menu_name__icontains=keyword)
    return render(request,"services.html",{"services":services})

def services(request):

    return render(request,"services.html")


def service_list(request):
    services=Service.objects.all()
    return render(request,'services.html',{'services':services})

class ServiceListView(ListView):
    model=Service

class ServiceDetailView(DetailView):
    model=Service
    template_name="services/servicedetail.html"


class CategoryDetailView(DetailView):
    model=Category
    template_name="category/category_detail.html"
    slug_field="category_slug"
    context_object_name="category_obj"