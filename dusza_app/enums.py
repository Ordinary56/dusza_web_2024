from django.db import models
from django.utils.translation import gettext_lazy as _

'''
Any necessary enums that exists in the database are defined here
'''

class RoleEnum(models.IntegerChoices):
        TEAM = 0, _("CSAPAT")
        ORGANIZER = 1, _("SZERVEZŐ")
        SCHOOL = 2, _("ISKOLA")