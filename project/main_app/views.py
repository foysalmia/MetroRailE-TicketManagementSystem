from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def wellcome(request):
    data = {
        'title' : 'Home page'
    }
    return HttpResponse("<h1>Wellcome everyone !</h1>")