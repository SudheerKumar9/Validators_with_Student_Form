from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *

def stuform(request):
    SFO=StudenForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFD=StudenForm(request.POST)
        if SFD.is_valid():
            return HttpResponse('Valid Data')
        else:
            return HttpResponse('Invalid Data')


    return render(request,'stuform.html',d)