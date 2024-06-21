from django.shortcuts import render
from ecommerceapp.models import Contact,Product
from django.contrib import messages
from math import ceil

# Create your views here.
#def index(request):
    
def index(request):
      allProds = []
      prods = Product.objects.all()
      n = len(prods)
      nSlides = n//4 + ceil((n/4)-(n//4))
      allProds.append([prods, range(1, nSlides), nSlides])

      params = {'allProds': allProds}

      return render(request, "index.html", params)
    
    
    
def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        message=request.POST.get("message")
        phone=request.POST.get("phone")
        myquery=Contact(name=name,email=email,message=message,phone=phone)
        myquery.save()
        messages.info(request,"we will get back to you soon...")
        #return render(request,"contact.html")

    return render(request,"contact.html")
