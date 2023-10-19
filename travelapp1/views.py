from django.shortcuts import render
from . models import place
from . models import arun
# Create your views here.
# def fun1(request):
#     arun1=arun.objects.all()
    # return render(request,"index.html",{'aruns':arun1})

def fun(request):
    obj=place.objects.all()
    arun1 = arun.objects.all()
    return render(request,"index.html",{'results':obj,'aruns':arun1})

def addition(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    num3=num1+num2
    return render(request,"result.html",{"add":num3})
