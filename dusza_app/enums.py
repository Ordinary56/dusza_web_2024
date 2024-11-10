from django.db import models
from django.utils.translation import gettext_lazy as _
class RoleEnum(models.IntegerChoices):
        TEAM = 0, 
        ORGANIZER = 1, 
        SCHOOL = 2,
        ADMIN = 3

class StatusEnum(models.IntegerChoices):
        REGISTRATED = 0, _("Regisztrált")
        APPROVED_BY_SCHOOL = 1, _("Tanárok által jóváhagyva")
        APPROVED_BY_ORGANIZERS = 2, _("Szervezők által jóváhagyva")