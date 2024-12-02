from django.shortcuts import render
from .models import Service,Category
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required



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
    return render(request,"services/service_list.html",{"object_list":services})


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


    # crud===>
@method_decorator(staff_member_required,name="dispatch")
class ServiceCreateView(CreateView):
    model= Service
    fields="__all__"
    success_url="/services"

@method_decorator(staff_member_required,name="dispatch")
class ServiceUpdateView(UpdateView):
    model =Service
    fields="__all__"
    success_url="/services"

#+=================================================
@method_decorator(staff_member_required,name="dispatch")
class ServiceDeleteView(DeleteView):
    model=Service
    success_url="/services"