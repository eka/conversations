from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey('auth.User', unique=True)

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __unicode__(self):
        pass
