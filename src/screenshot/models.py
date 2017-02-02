from __future__ import unicode_literals

from django.db import models

# Create your models here.


class ScreenShot(models.Model):
    file = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return str(self.created)


class OrbMatcher(models.Model):
    screenshot = models.OneToOneField(ScreenShot)
    status = models.CharField(max_length=20, default="none")
    confidence = models.FloatField(default=0)

    def __unicode__(self):
        return "%s:%s" % (self.status, self.confidence)


class ImageHash(models.Model):
    screenshot = models.OneToOneField(ScreenShot)
    ahash = models.CharField(max_length=100)
    phash = models.CharField(max_length=100)
    dhash = models.CharField(max_length=100)
    whash = models.CharField(max_length=100)

    def __unicode__(self):
        return unicode(self.screenshot)
