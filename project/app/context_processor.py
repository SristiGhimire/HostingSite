from . models import *

def footer(request):
    footer = CompanyDetails.objects.first()
    return{
        'footer':footer
    }

def service(request):
    service = Service.objects.all()
    return{
        'service':service
    }

def about(request):
    about = About.objects.first()
    return{
        'about': about
    }

def hosting(request):
    hosting = Hosting.objects.all()[:3]
    return{
        'hosting': hosting
    }