from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)

# Create your models here.

class UserManager(BaseUserManager):

    #We are overwriting the current method
    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError('Users should have a username')

        if email is None:
            raise TypeError('Users should have an Email')

        #Define how user should be created
        user = self.model(username=username, email=self.normalize_email(email))

        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, username, email, password=None):

        if password is None:
            raise TypeError('Password should not be none')

        print("I'm Creating superusernow")
        #Define how user should be created
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

#Abstract base user(regular user)
class User(AbstractBaseUser, PermissionsMixin):
    #Db_index = search in DB by using username
    username=models.CharField(max_length = 255, unique=True, db_index = True)
    email = models.EmailField(max_length = 255, unique=True, db_index = True)
    #Verified account or not
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

    def tokens(self):
        return ''

