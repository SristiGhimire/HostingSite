from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views.generic.base import View
from .forms import *
from django.contrib import auth
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'app2/index.html')

def addservice(request):
    addservice = AddService.objects.all()
    context = {"addservice": addservice}
    return render(request, 'app2/addservice.html', context)


def team(request):
    return render(request, 'app2/ourTeam.html')




def add_edit_Hosting(request, id=None):
    instance = None
    try:
        if id:
            instance = Hosting.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Hosting.')
        return redirect('dashboard:add_Hosting')
    if request.method == 'POST':
        form = HostingForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Service edited successfully.')
                return redirect('dashboard:edit_Hosting', id=instance.id)  # Redirect to the edited Hosting's details page
            else:  # Add operation
                messages.success(request, 'Hosting added successfully.')
                return redirect('dashboard:add_Hosting')  # Redirect to the page for adding new Hostings
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = HostingForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Hosting.html', context)

class HostingListView(View):
    template_name = 'app2/Hosting.html'
    def get(self, request):
        prod = Hosting.objects.all()
   
        return render(request, self.template_name, {'details': prod})

class HostingDeleteView(View):
    template_name = 'app2/Hosting.html'
    def get(self, request, id):
        record = get_object_or_404(Hosting, id=id)
        return render(request, self.template_name, {'details': record})
    def post(self, request, id):
        record = get_object_or_404(Hosting, id=id)
        record.delete()
        return redirect('dashboard:Hosting')



def add_edit_About(request):
    instance = None
    try:
        if id:
            instance = About.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the About.')
        return redirect('dashboard:add_About')
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'About edited successfully.')
                return redirect('dashboard:add_About')  # Redirect to the added About's details page
            else:  # Add operation
                messages.success(request, 'About added successfully.')
                return redirect('dashboard:add_About')  # Redirect to the page for adding new Abouts
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = AboutForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_about.html', context)



def add_edit_Question(request, id=None):
    instance = None
    try:
        if id:
            instance = Question.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Question.')
        return redirect('dashboard:add_Question')
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Service edited successfully.')
                return redirect('dashboard:edit_Question', id=instance.id)  # Redirect to the edited Question's details page
            else:  # Add operation
                messages.success(request, 'Question added successfully.')
                return redirect('dashboard:add_Question')  # Redirect to the page for adding new Questions
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = QuestionForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Question.html', context)

class QuestionListView(View):
    template_name = 'app2/Question.html'
    def get(self, request):
        prod = Question.objects.all()
   
        return render(request, self.template_name, {'details': prod})

class QuestionDeleteView(View):
    template_name = 'app2/Question.html'
    def get(self, request, id):
        record = get_object_or_404(Question, id=id)
        return render(request, self.template_name, {'details': record})
    def post(self, request, id):
        record = get_object_or_404(Question, id=id)
        record.delete()
        return redirect('dashboard:Question')


def add_edit_Client(request, id=None):
    instance = None
    try:
        if id:
            instance = Client.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Client.')
        return redirect('dashboard:add_Client')
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Service edited successfully.')
                return redirect('dashboard:edit_Client', id=instance.id)  # Redirect to the edited Client's details page
            else:  # Add operation
                messages.success(request, 'Client added successfully.')
                return redirect('dashboard:add_Client')  # Redirect to the page for adding new Clients
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = ClientForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Client.html', context)

class ClientListView(View):
    template_name = 'app2/Client.html'
    def get(self, request):
        prod = Client.objects.all()
   
        return render(request, self.template_name, {'details': prod})

class ClientDeleteView(View):
    template_name = 'app2/Client.html'
    def get(self, request, id):
        record = get_object_or_404(Client, id=id)
        return render(request, self.template_name, {'details': record})
    def post(self, request, id):
        record = get_object_or_404(Client, id=id)
        record.delete()
        return redirect('dashboard:Client')



def HeroBanners(request):
    instance = None
    try:
        if id:
            instance = HeroBanner.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the HeroBanner.')
        return redirect('dashboard:HeroBanner')
    if request.method == 'POST':
        form = HeroBannerForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'HeroBanner edited successfully.')
                return redirect('dashboard:add_HeroBanner')  # Redirect to the edited HeroBanner's details page
            else:  # Add operation
                messages.success(request, 'HeroBanner added successfully.')
                return redirect('dashboard:add_HeroBanner')  # Redirect to the page for adding new HeroBanner
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = HeroBannerForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_HeroBanner.html', context)


def CompanyDetailss(request):
    instance = None
    try:
        if id:
            instance = CompanyDetails.objects.first()
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the CompanyDetails.')
        return redirect('dashboard:CompanyDetails')
    if request.method == 'POST':
        form = CompanyDetailsForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'CompanyDetails edited successfully.')
                return redirect('dashboard:add_CompanyDetails')  # Redirect to the edited CompanyDetails's details page
            else:  # Add operation
                messages.success(request, 'CompanyDetails added successfully.')
                return redirect('dashboard:add_CompanyDetails')  # Redirect to the page for adding new CompanyDetails
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = CompanyDetailsForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_CompanyDetails.html', context)



def add_edit_Service(request, id=None):
    instance = None
    try:
        if id:
            instance = Service.objects.get(pk=id)
    except Exception as e:
        messages.warning(request, 'An error occurred while retrieving the Service.')
        return redirect('dashboard:add_Service')
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            if instance:  # Edit operation
                messages.success(request, 'Service edited successfully.')
                return redirect('dashboard:edit_Service', id=instance.id)  # Redirect to the edited Service's details page
            else:  # Add operation
                messages.success(request, 'Service added successfully.')
                return redirect('dashboard:add_Service')  # Redirect to the page for adding new Services
        else:
            messages.warning(request, 'Form is not valid. Please correct the errors.')
    else:
        form = ServiceForm(instance=instance)
    context = {'form': form, 'instance': instance}
    return render(request, 'app2/create_Service.html', context)

class ServiceListView(View):
    template_name = 'app2/Service.html'
    def get(self, request):
        prod = Service.objects.all()
   
        return render(request, self.template_name, {'details': prod})

class ServiceDeleteView(View):
    template_name = 'app2/Service.html'
    def get(self, request, id):
        record = get_object_or_404(Service, id=id)
        return render(request, self.template_name, {'details': record})
    def post(self, request, id):
        record = get_object_or_404(Service, id=id)
        record.delete()
        return redirect('dashboard:Service')


# for logout
def userlogout(request):
    auth.logout(request)
    messages.info(request, "logout successfully..")
    return redirect('app:signin')