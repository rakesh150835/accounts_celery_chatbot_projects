from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from PIL import Image


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name=None, password=None):
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(email=self.normalize_email(email),
                          first_name = first_name,
                          last_name = last_name,
                          )

        user.set_password(password)
    
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name=None, password=None):
        user = self.create_user(email=email,
                                 first_name=first_name, 
                                 last_name=last_name,
                                  password=password)
        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)
        return user
    

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    

 
 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='images/profile_pics')
 
    def __str__(self):
        return f'{self.user.first_name} Profile'
