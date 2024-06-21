from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def signup(request):
    
    if request.method == "POST":
        name=request.POST['firstName']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirmPassword']
        if password != confirm_password:
            messages.warning(request,"Password is not Matching")
            return render(request,'signup.html')
    
        try:
            if User.objects.get(username=email):
                   messages.warning(request,"Email is  Taken")
                   return render(request,'signup.html')
            
        except Exception as identifier:
            pass
        
        user = User.objects.create_user(email,name,password)
        user.save()
        messages.warning(request,"User Created Successfully")   

    
    return render(request,"signup.html")



def handlelogin(request):
    if request.method == "POST":
        
        username = request.POST['email']
        userpassword = request.POST['password']
        myuser = authenticate(username=username,password=userpassword)
        
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')
        
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/auth/login')

    return render(request,"login.html")



def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Success")
    return redirect('/auth/login')