from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer']
    ordering = ['-id']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['-id']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['url']
    ordering = ['-id']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject']
    ordering = ['-id']

@admin.register(CompanyDetails)
class CompanyDetailsAdmin(admin.ModelAdmin):
    list_display = ['companyAddress', 'companyPhone', 'companyEmail', 'addressUrl']
    ordering = ['-id']



# Define the TabularInline for HostingPackage
class HostingPackageInline(admin.TabularInline):
    model = HostingPackage
    extra = 1  # Number of extra forms to display

# Register your models here.

@admin.register(Hosting)
class HostingAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['-id']
    inlines = [HostingPackageInline]

@admin.register(HostingPackage)
class HostingPackageAdmin(admin.ModelAdmin):
    list_display = ['hosting', 'selectPackages', 'storage', 'bandwidth', 'support', 'domain', 'accountResold', 'feePerMonth']
    ordering = ['-id']

@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    ordering = ['-id']


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ['name','email','password1','password2']
    ordering = ['-id']