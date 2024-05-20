from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views.generic.base import View
from .forms import *
from django.contrib import auth
from django.contrib import messages
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
    return render(request, 'app2/index.html')

def addservice(request):
    addservice = AddService.objects.all()
    context = {"addservice": addservice}
    return render(request, 'app2/addservice.html', context)


def team(request):
    return render(request, 'app2/ourTeam.html')


def create_or_edit_hosting(request, hosting_id=None):
    if hosting_id:
        hosting_instance = get_object_or_404(Hosting, id=hosting_id)
        HostingPackageFormSet = inlineformset_factory(Hosting, HostingPackage, form=HostingPackageForm, extra=1)
    else:
        hosting_instance = Hosting()
        HostingPackageFormSet = inlineformset_factory(Hosting, HostingPackage, form=HostingPackageForm,extra=1)
    if request.method == 'POST':
        hosting_form = HostingForm(request.POST, instance=hosting_instance)
        formset = HostingPackageFormSet(request.POST, instance=hosting_instance)
        if hosting_form.is_valid() and formset.is_valid():
            hosting_instance = hosting_form.save()
            formset.instance = hosting_instance
            formset.save()
            if hosting_id:
                messages.success(request, 'Hosting Updated successfully.')
                return redirect('dashboard:edit_Hosting', hosting_id=hosting_instance.id)
            else:
                messages.success(request, 'Hosting added successfully.')
                return redirect('dashboard:add_Hosting')
    else:
        hosting_form = HostingForm(instance=hosting_instance)
        formset = HostingPackageFormSet(instance=hosting_instance)
    context = {
        'hosting_form': hosting_form,
        'formset': formset,
        'is_inline_formset_used': True,
    }
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
    return redirect('dashboard:signin')


# def login(request):
#     try:
#         if request.user.is_authenticated:
#             return render(request,'app2/index.html')
#         if request.method =="POST":
#             email = request.POST['useremail']
#             print(email)
#             password = request.POST['password']
#             print(password)
#             # user_obj = User.objects.filter(email=email)
#             user_obj = authenticate(email=email, password=password)
#             print(user_obj)
#             if not user_obj: #not user_obj.exists():
#                 messages.warning(request,"Invalid username and password...")
#                 return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#             user_obj = authenticate(email=email, password=password)
#             if user_obj and user_obj.is_admin or user_obj.is_editor:
#                 auth.login(request, user_obj)
#                 return redirect('dashboard:index')
#             messages.warning(request,'Inavlid Password')
#             return redirect('dashboard:login')
#         return render(request,'app2/login.html')
#     except Exception as e:
#         print(e)
#         messages.warning(request,'something wrong...')
#         return redirect('dashboard:login')



def signin(request):
    try:
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return render(request, 'app2/index.html')
            else:
                messages.warning(request, "You do not have permission to access this page.")
                return redirect('dashboard:login')
        
        if request.method == "POST":
            email = request.POST.get('useremail')
            password = request.POST.get('password')

            # Ensure that authenticate uses email for the username field
            user_obj = authenticate(request, username=email, password=password)
            
            if user_obj is None:
                messages.warning(request, "Invalid username or password.")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            
            if user_obj.is_superuser:
                auth.login(request, user_obj)
                return redirect('dashboard:index')
            else:
                messages.warning(request, "You do not have permission to access this page.")
                return redirect('dashboard:login')
        
        return render(request, 'app2/sign-in.html')

    except Exception as e:
        print(e)
        messages.warning(request, 'Something went wrong...')
        return redirect('dashboard:signin')

