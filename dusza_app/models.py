from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from dusza_app.enums import RoleEnum

# Create your models here.

class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        return super().get_by_natural_key(username=username)
    def create_user(self, username, password,**extra_fields):
        if not username or not password:
            raise ValueError("A felhasználónevet és jelszót muszáj beállítanod")
        user = self.model(username=username, password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password=None, **extra_fields):
        """Create and return a superuser with a username and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

'''
All database models are defined here
'''
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=128, blank=True, default='') 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    role = models.IntegerField(choices= RoleEnum,
                               default= RoleEnum.TEAM)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True)
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    def save(self, *args, **kwargs):
        if(self.password):
            self.password = make_password(self.password, salt='$^13_2',
                                          hasher='')
        super().save(*args, **kwargs)
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    def has_module_perms(self, app_label):
        return self.is_superuser
    def __str__(self):
        return self.username

# Categories which teams can choose 
class Category(models.Model):
    category = models.CharField(max_length=255, primary_key=True)

# Short for programming languages
class ProgLangs(models.Model):
    language = models.CharField(max_length=255, primary_key=True)

class School(models.Model):
    id = models.AutoField(primary_key=True)
    schoolName = models.CharField(max_length=255)
    schoolAddress = models.CharField(max_length=255)
    principalName = models.CharField(max_length=255)
    principalEmail = models.EmailField()

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    # Associated user
    teamName = models.CharField(max_length=30)
    mentor = models.CharField(max_length=30)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

class TeamMember(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    term = models.CharField(max_length=20)
    extraMember = models.BooleanField(default= False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
