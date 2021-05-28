# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.forms import UsernameField
from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.admin import UserAdmin


# Create your models here.

# class MyManager(BaseUserManager):
#     def create_user(self, username, email, displayname, age, homepage, password=None):
#         if not age:
#             raise ValueError("Please input a number for your age.")
#         if not displayname:
#             raise ValueError("Users must have a displayname")
#         if not username:
#             raise ValueError("Users must have a valid username")

#         user = self.model(
#             username=username,
#             email=self.normalize_email(email),
#             displayname=displayname,
#             age=age,
#             homepage=homepage,
#             password=None)

#     def create_superuser(self, username, email, displayname, age, homepage, password=None):
#         user = self.model(
#             username=username,
#             email=self.normalize_email(email),
#             displayname=displayname,
#             age=age,
#             homepage=homepage,
#             password=password,
#         )
#         user.isadmin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self.db)

class MyUser(AbstractUser):
    
    displayname = models.CharField(max_length=30)
    age = models.IntegerField(blank=False)
    homepage = models.URLField(null=True, blank=True)

    REQUIRED_FIELDS = ["age"]
    
    # objects = MyManager()



