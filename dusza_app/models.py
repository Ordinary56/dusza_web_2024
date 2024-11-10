from typing import Collection
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from dusza_app.enums import RoleEnum, StatusEnum

# Create your models here.
class DeadLine(models.Model):
    startDate = models.DateField(primary_key=True, unique=True)
    endDate = models.DateField(unique=True)


class User(AbstractUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    role = models.IntegerField(choices= RoleEnum, default= RoleEnum.TEAM)
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
    def __str__(self) -> str:
        return self.category

# Short for programming languages
class ProgLangs(models.Model):
    language = models.CharField(max_length=255, primary_key=True)
    def __str__(self) -> str:
        return self.language

class School(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=255)
    school_address = models.CharField(max_length=255)
    principal_name = models.CharField(max_length=255)
    principal_email = models.EmailField()
    def __str__(self) -> str:
        return self.school_name

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    # Associated user
    team_name = models.CharField(max_length=30)
    mentor = models.CharField(max_length=30)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    programming_language = models.ForeignKey(ProgLangs, on_delete=models.CASCADE, blank=True, null=True)
    status = models.IntegerField(choices=StatusEnum, default=StatusEnum.REGISTRATED)

class TeamMember(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    term = models.CharField(max_length=20)
    extra_member = models.BooleanField(default= False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)
