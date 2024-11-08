from django.db import models

from dusza_app.enums import RoleEnum

# Create your models here.
'''
All database models are defined here
'''
class User(models.Model):
    Id = models.IntegerField(primary_key=True)
    Username = models.CharField(255)
    Password = models.CharField(255)
    Role = models.IntegerField(max_length= 2,
                               choices= RoleEnum,
                               default= RoleEnum.TEAM)

# Categories which teams can choose 
class Category(models.Model):
    Category = models.CharField(255, primary_key=True)

# Short for programming languages
class ProgLangs(models.Model):
    Language = models.CharField(255, primary_key=True)

class School(models.Model):
    Id = models.IntegerField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    SchoolName = models.CharField(255)
    SchoolAddress = models.CharField(255)
    PrincipalName = models.CharField(255)
    PrincipalEmail = models.EmailField()

class Team(models.Model):
    Id = models.IntegerField(primary_key=True)
    # Associated user
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    TeamName = models.CharField(30)
    Mentor = models.CharField(30)
    School = models.ForeignKey(School, on_delete=models.CASCADE)

class TeamMember(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(30)
    Term = models.CharField(20)
    ExtraMember = models.BooleanField(default=  False)

