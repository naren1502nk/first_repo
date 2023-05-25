from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_string(request):
    return HttpResponse('this is my first view')

def naren(request):
    return render(request,'naren.html')
