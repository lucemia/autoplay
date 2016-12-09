from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ScreenShot(models.Model):
    file = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.created)
