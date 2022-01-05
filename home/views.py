from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
      #return HttpResponse('Madhusudan Sharma. Kathmandu, Nepal')
      return render (request, 'index.html')
      messages.success(request, 'Contact Info Submitted.')

def contact(request):
     if request.method == 'POST':
        fname = request.POST.get('fname')
        lname= request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        contact=Contact(fname=fname,lname=lname,email=email,phone=phone,date=datetime.today())
        contact.save()
        messages.success(request, 'Contact Info Submitted.')

     context={'name': 'Madhusudan Sharma',
            'phone':9854755887,
            'address':'Kathmandu, Nepal',
            }
    
     return render (request, 'contact.html', context)
   
def about(request):
    return render (request, 'about.html')