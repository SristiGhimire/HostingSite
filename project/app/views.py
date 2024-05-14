from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib.auth.models import User


def index(request):
    # herobanner = HeroBanner.objects.first()
    # question = Question.objects.all()[:4]
    # hosting = Hosting.objects.all()
    # about = About.objects.first()
    # service = Service.objects.all()[:3]
    # client = Client.objects.all()

    # context = {"question": question, "hosting": hosting, "about":about, "service": service, "client":client, "herobanner": herobanner}
    return render(request, 'app/index.html')

def contact(request):
    return render(request, 'app/contact.html')

def about(request):
    return render(request, 'app/about.html')

def service(request):
    return render(request, 'app/service.html')

def serviceDetail(request):
    # item = Service.objects.get(id=id)
    return render(request, 'app/serviceDetail.html')



