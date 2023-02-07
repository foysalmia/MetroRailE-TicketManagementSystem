from django.shortcuts import render,HttpResponse
from base.models import server

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("this is home page")

def about(request):
    return HttpResponse("this is about page")

def submit(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        p = request.POST.get("password")
        person = server(email= email, password = p)
        context = {"email":{email}}
        if( email != ""):
            person.save()
            return render(request,"submit.html",context)
        
    return HttpResponse("this is submit page\ Fill all fild")