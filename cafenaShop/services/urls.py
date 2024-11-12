from django.urls import path
from . import views

urlpatterns=[
    path('',views.ServiceListView.as_view(),name="services"),
    # ---------------------------------------------------------
    path('nicaragua-Whole-Bean/',views.nicaragua_Whole_Bean,name="nicaragua-Whole-Bean"),
    path('culumbia-Whole-Bean/',views.culumbia_Whole_Bean,name="culumbia-Whole-Bean"),
    path('peru-Whole-Bean/',views.peru_Whole_Bean,name="peru-Whole-Bean"),
    path('<int:pk>/',views.ServiceDetailView.as_view(),name="service-detail"),
    path('<slug:slug>/',views.CategoryDetailView.as_view(),name="category-detail"),
    path('search',views.search,name="search")
    
]