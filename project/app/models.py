from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields.files import ImageField 

# Create your models here.

class Service(models.Model):
    logo = models.ImageField(upload_to= 'Serviceimage/')
    title = models.CharField(max_length=200)
    description = RichTextField()
    image = models.ImageField(upload_to= 'Serviceimage/')
   
    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['-id']

class HostingService(models.Model):
    logo = models.ImageField(upload_to= 'HostingServiceimage/')
    title = models.CharField(max_length=200)
    description = RichTextField()
   
    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['-id']



class Question(models.Model):
    question = models.CharField(max_length=50)
    answer = RichTextField()

    def __str__(self):
        return self.question
 

class Hosting(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['-id']
        

selectPackage =(
    ('personal','Personal'),            
    ('business','Business'),
    ('enterprise','Enterprise'),
    ('standard','Standard'),
    ('premium','Premium'),
    ('gold','Gold'))        


class HostingPackage(models.Model):
    hosting= models.ForeignKey(Hosting,on_delete= models.SET_NULL,null=True, blank=True,  related_name ='hostings')
    selectPackages=models.CharField(max_length=150, choices=selectPackage)
    storage=models.CharField(max_length=200)
    bandwidth=models.CharField(max_length=200)
    support=models.CharField(max_length=200)
    domain=models.CharField(max_length=200)
    accountResold=models.PositiveIntegerField()
    feePerMonth=models.FloatField()
    
    def __str__(self):
        return self.selectPackages


    class Meta:
        ordering =['-id']



class About(models.Model):
    image=models.FileField(upload_to="aboutimage")
    title=models.CharField(max_length=200)
    description=RichTextField()

    def __str__(self):
        return self.title
    





class Client(models.Model):
    logo=models.FileField(upload_to="clientlogo")
    url=models.URLField()

    def __str__(self):
        return self.url
    
    class Meta:
        ordering =['-id']

class Contact(models.Model):
    name=models.CharField(max_length=200)
    surname=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering =['-id']


class CompanyDetails(models.Model):
    companyName = models.CharField(max_length=200)
    companyAddress=models.CharField(max_length=200)
    companyPhone=models.CharField(max_length=200)
    companyEmail=models.EmailField()
    addressUrl=models.URLField(max_length=2000)
    companyLogo=models.FileField(upload_to="companylogo")
    facebookUrl = models.URLField()
    linkedInUrl = models.URLField()
    twiterUrl = models.URLField()
    discordUrl = models.URLField()
    livechatUrl = models.URLField()
    companyDescription = models.TextField()
    gif = models.ImageField(upload_to="gif")

    def __str__(self):
        return self.companyAddress
    
    class Meta:
        ordering =['-id']



class HeroBanner(models.Model):
    image=models.FileField(upload_to="herobannerimage")
    title=models.CharField(max_length=200)
    description=RichTextField()

    def __str__(self):
        return self.title

class SignUp(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    password1=models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class SignIn(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.email

class Superuser(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username




