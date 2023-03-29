from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate
from home.models import User
from home.models import UserDetails
# Create your views here.
def index(request):
    # return HttpResponse("hi")
    # sd = User.objects.all()
    # a ={
    #     "a":sd
    # }
    # if request.method == "POST":
    #      pass1 = request.POST.get('pass')
    #      email = request.POST.get('email')
         
         
    #      contact = User(email=email,pass1=pass1)
    #      contact.save()
        #  return redirect('/')
        if request.method == 'POST':
            email = request.POST.get('email')
            Fn = request.POST.get('fn')
            desc = request.POST.get('email')
            
            Ud = UserDetails(fn = Fn,email=email,desc=desc)
            Ud.save()
     
        return render(request,'a.html')
# def signup(request):
#     sd = User.objects.all()
#     ab={
#     "a":sd
#       }
#     return render(request,'apphost.html',ab)
   
    
def home(request):
    ssd = UserDetails.objects.all()
    ds ={
        "vs":ssd
    }
    return render(request,'apphost.html',ds)
    
def delete(request,id):
        dele = User.objects.get(id=id)
        dele.delete() 
        return redirect('/home')
        
    