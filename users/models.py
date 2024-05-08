from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid

class MyCustomManager (BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email or Username must be set!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields): 
        extra_fields.setdefault('is_staff', True) 
        extra_fields.setdefault('is_superuser', True) 
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True') 
        if extra_fields.get('is_superuser') is not True: 
            raise ValueError('Superuser must have is_superuser=True') 
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=False)

    is_staff = models.BooleanField( 
        gettext_lazy('I am staff'),
        default=False,
    help_text = gettext_lazy('If the user is admin stuff of this site then can see admin panel')
    )
    is_active = models.BooleanField(
        gettext_lazy('account active'),
        default=True,
        help_text=gettext_lazy('A user should be treated as active. Admin can unselect this instead of deleting accounts')
    )

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='admin',  
    )

    def is_admin(self):
        return self.role == 'admin'

    def is_customer(self):
        return self.role == 'customer'

    USERNAME_FIELD = 'email'
    
    objects = MyCustomManager()

    def __str__(self): 
        return f"USER - {self.email}"
    def get_full_name(self): 
        return self.email
    def get_short_name(self): 
        return self.email


class CommonBaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, default= uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Profile(CommonBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    details_filled = models.BooleanField(default=False)
    image = models.ImageField(upload_to="UserImages",default="default.jpg")
    age = models.DateField(auto_now=False, auto_now_add=False, null=True)
    address = models.CharField( max_length=500,null=True)
    
    
    def is_fully_filled(self):
        fields_names = [f.name for f in self._meta.get_fields()]
        for field_name in fields_names:
            value = getattr(self, field_name) 
            if value is None or value=='':
                return False
        return True
    
    def __str__(self): 
        return f"profile - {self.user}"
    
@receiver(post_save, sender=User) 
def create_profile(sender, instance, created, **kwargs): 
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User) 
def save_profile(sender, instance, **kwargs): 
    instance.profile.save()
