from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate,login,logout

# create views here...
def home (request):
    return render(request,"index.html")


def user_login(request):
    if request.method=="GET":
        return render(request,"login.html")
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print(request.user.first_name)
            return HttpResponseRedirect("/services")
        else:
            return render(request,"login.html",{"message":"log in failed"})
        

# =======================logout page =================================================
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/login")


#=========================Register Page ==========================

def register(request):
    if request.method=="GET":
        # form=UserCreationForm()
        form=CustomUserCreationForm()
        return render(request,"register.html",{"form":form})
    else:
        # submited_form=UserCreationForm(request.POST)
        submited_form=CustomUserCreationForm(request.POST)
        if submited_form.is_valid():
            submited_form.save()
            return HttpResponseRedirect("/login")
        return render(request,"register.html",{"form":submited_form})


