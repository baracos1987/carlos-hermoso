from django.shortcuts import render
from django.http import HttpResponse #Profe......
from .models import contactenos #profe....
import requests #profe...
import json #profe....
#import email
#from email.message import Message
#import re


# 1 ejercicio:
    #def index (request):
    #    return HttpResponse('Hola mundo')

# 2 ejercicio :
def index (request):
    return render(request,'misitio/Rodamientos.html') 

def Rodamientos (request):
    return render(request,'misitio/index.html')

def contact (request):
    if request.method == 'POST':
        email_r = request.POST.get('email') #Email_r es una variable que creamos igual que las otras
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')
        c = contactenos(email=email_r, Subject=subject_r, Message=message_r)
        c.save()
       
        return render(request, 'misitio/agradecimiento.html') #retomamoss al sitio nuevamente contacto.html
    else:
        return render(request,'misitio/contactenos.html')    


