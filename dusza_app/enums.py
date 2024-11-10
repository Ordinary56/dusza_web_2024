from django.db import models
from django.utils.translation import gettext_lazy as _

'''
Any necessary enums that exists in the database are defined here
'''

class RoleEnum(models.IntegerChoices):
        TEAM = 0, 
        ORGANIZER = 1, 
        SCHOOL = 2,
        ADMIN = 3