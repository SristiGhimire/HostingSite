from django import forms
from app .models import *


class HostingForm(forms.ModelForm):
    class Meta:
        model = Hosting
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'


class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = '__all__'

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class HeroBannerForm(forms.ModelForm):
    class Meta:
        model = HeroBanner
        fields = '__all__'

class CompanyDetailsForm(forms.ModelForm):
    class Meta:
        model = CompanyDetails
        fields = '__all__'