from django.urls import path
from . import views

urlpatterns=[
    path('',views.ServiceListView.as_view(),name="services"),
    # ---------------------------------------------------------
   
    path('<int:pk>/',views.ServiceDetailView.as_view(),name="service-detail"),
    path('search',views.search,name="search"),
    path('service-create/',views.ServiceCreateView.as_view(),name="menu-create"),
    path('update-service/<int:pk>/',views.ServiceUpdateView.as_view(),name="menu-update"),
    path('delete-service/<int:pk>/',views.ServiceDeleteView.as_view(),name="menu-delete"),
        path('<slug:slug>/',views.CategoryDetailView.as_view(),name="category-detail"),

]