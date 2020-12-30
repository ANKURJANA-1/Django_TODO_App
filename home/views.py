from django.shortcuts import render
from .models import Data

# Create your views here.
def home(request):
    return render(request,'home/index.html')


def submit(request):

    obj=Data()
    obj.content=request.POST["content"]
    obj.save()
    data=Data.objects.all()
    return render(request,'home/index.html',{'data':data})

def seen(request):
    pass 
         

    
