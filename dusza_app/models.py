from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from dusza_app.enums import RoleEnum

# Create your models here.



class User(AbstractUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    role = models.IntegerField(choices= RoleEnum,
                               default= RoleEnum.TEAM)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, null=True, blank=True)
    school = models.ForeignKey('School', on_delete=models.CASCADE, null=True, blank=True)
    username_validator = UnicodeUsernameValidator(
        r'^[\w @+.-]+$',
        "Egy érvényes felhasználónév csak betűkből, számokból, szóközökből és az alábbi speciális karakterkből állhat: [^,$,@,&] (maximum karakterszám: 150)"
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[username_validator],
    )
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
