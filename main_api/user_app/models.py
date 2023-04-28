from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone

# Create your models here.
class UserManager(BaseUserManager):
# user object creation and the fields needed for that

    # private method
    def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):

        now = timezone.now()

        if not username:
            raise ValueError("That username is not valid.")
        
        # convert domain part of email to lowercase
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser, date_joined=now, **extra_fields)
        # can also set some of these manually, for example with is_active=False until they verify their email.

        user.set_password(password)
        user.save(using=self._db)

        return user

    # public method to create normal user
    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, is_active=True, is_staff=False, is_superuser=False, **extra_fields)
    
    def create_superuser(self, username, email, password, **extra_fields):

        user = self._create_user(username, email, password, is_active=True, is_staff=True, is_superuser=True, **extra_fields)

        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # can add these because of **extra_fields
    date_joined = models.DateTimeField(default=timezone.now)
    # removed () from timezone.now() above because of warning:
    # user_app.User.date_joined: (fields.W161) Fixed default value provided.
	#     HINT: It seems you set a fixed date / time / datetime value as default for this field. This may not be what you want. If you want to have the current date as default, use `django.utils.timezone.now`

    receive_newsletter = models.BooleanField(default=False)
    birth_date = models.DateTimeField(blank=True, null=True)
    about_me = models.TextField(max_length=500, blank=True, null=True)
    # profile_img = models.ImageField(null=True) 
    # ^ temporarily removed due to error:
    # user_app.User.profile_img: (fields.E210) Cannot use ImageField because Pillow is not installed.
    #     HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".


    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
    ]