from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings 
from django.contrib.auth.models import User


def index(request):
    herobanner = HeroBanner.objects.first()
    question = Question.objects.all()
    # about = About.objects.first()
    service = Service.objects.all()[:4]
    client = Client.objects.all()
    contact = Contact.objects.all()

    # context = {"question": question, "hosting": hosting, "about":about, "service": service, "client":client, "herobanner": herobanner}
    context={"herobanner": herobanner, "service": service, "client":client, "question": question, "contact": contact}
    return render(request, 'app/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST['email']
        message = request.POST['message']
        contact_obj = Contact(name = name, surname = surname, email = email, message = message)
        contact_obj.save()
        
        # send mail with customer query
        subject = "New Contact Form Submission"
        message =f"User Name : {name}\nUser Surname : {surname}\nmessage : {message}"
        email_from = settings.EMAIL_HOST_USER
        user_email = [email]
        send_mail(subject, message, email_from, user_email)
        return redirect('app:contact')
 
        
    else:
        return render(request, 'app/contact.html')

def about(request):
    return render(request, 'app/about.html')

def hosting(request):
    return render(request, 'app/hosting.html')

def service(request):
    return render(request, 'app/service.html')

def serviceDetail(request, id):
    item = Service.objects.get(id=id)
    relatedservice = Service.objects.all()[:3]
    return render(request, 'app/serviceDetail.html',{'item':item, 'relatedservice' : relatedservice})



