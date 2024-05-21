from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, phone_No, password=None):
        if not email:
            raise ValueError('User must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            firstname=firstname,
            lastname=lastname,
            phone_No=phone_No
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, firstname, lastname, phone_No, password=None):
        user = self.create_user(
            email,
            firstname=firstname,
            lastname=lastname,
            phone_No=phone_No,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    is_subAdmin = models.BooleanField(default=False)
    phone_No = models.CharField(max_length=150, null=True, blank=True)
    avatar = models.ImageField(upload_to="avatarimage/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname','lastname', 'phone_No']
    def __str__(self):
        return self.firstname

    @property
    def is_staff(self):
        return self.is_admin or self.is_user