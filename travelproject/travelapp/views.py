from django.http import HttpResponse
from django.shortcuts import render
from .models import place, photoc


# Create your views here.

def demo(requset):
    obj=place.objects.all()
    obj1=photoc.objects.all()

    return render(requset,"index.html",{'result':obj,'result1':obj1})

def news(request):
    return render(request,"news.html")

# def addition (request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
#
# def contact(request):
#     return HttpResponse("This is contact page")