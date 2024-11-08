from django.db import models

from dusza_app.enums import RoleEnum

# Create your models here.
'''
All database models are defined here
'''
class User(models.Model):
    Id = models.IntegerField(primary_key=True)
    Username = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    Role = models.IntegerField(max_length = 2,
                               choices= RoleEnum,
                               default= RoleEnum.TEAM)

# Categories which teams can choose 
class Category(models.Model):
    Category = models.CharField(max_length=255, primary_key=True)

# Short for programming languages
class ProgLangs(models.Model):
    Language = models.CharField(max_length=255, primary_key=True)

class School(models.Model):
    Id = models.IntegerField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    SchoolName = models.CharField(max_length=255)
    SchoolAddress = models.CharField(max_length=255)
    PrincipalName = models.CharField(max_length=255)
    PrincipalEmail = models.EmailField()

class Team(models.Model):
    Id = models.IntegerField(primary_key=True)
    # Associated user
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    TeamName = models.CharField(max_length=30)
    Mentor = models.CharField(max_length=30)
    School = models.ForeignKey(School, on_delete=models.CASCADE)

class TeamMember(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    Term = models.CharField(max_length=20)
    ExtraMember = models.BooleanField(default=  False)

