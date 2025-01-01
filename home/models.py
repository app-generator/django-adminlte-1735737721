# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Words(models.Model):

    #__Words_FIELDS__
    category = models.TextField(max_length=255, null=True, blank=True)
    word = models.TextField(max_length=255, null=True, blank=True)
    definition = models.TextField(max_length=255, null=True, blank=True)

    #__Words_FIELDS__END

    class Meta:
        verbose_name        = _("Words")
        verbose_name_plural = _("Words")


class Results(models.Model):

    #__Results_FIELDS__
    testdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    word_result = models.TextField(max_length=255, null=True, blank=True)

    #__Results_FIELDS__END

    class Meta:
        verbose_name        = _("Results")
        verbose_name_plural = _("Results")



#__MODELS__END
