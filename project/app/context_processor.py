from . models import *

def footer(request):
    footer = CompanyDetails.objects.first()
    return{
        'footer':footer
    }