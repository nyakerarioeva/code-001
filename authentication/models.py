from django.db import models

from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, profession,username,password=None):
        
        
        if not email:
            raise ValueError("email is required")
        if not profession:
            raise ValueError("Please provide your profession")
        if not username:
            raise ValueError("username is required")
class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email_address", max_length=60, unique=True)
    profession = models.CharField(verbose_name="profession", max_length=200,unique=True)
    username = models.CharField(verbose_name="username", max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ['profession','username']
    
    def __str__(self):
        return str(self.username)
    
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    