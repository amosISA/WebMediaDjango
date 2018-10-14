from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating
    ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

class Video(TimeStampedModel):
    VideoID = models.IntegerField
    Path = models.CharField(max_length=100, null = False, blank = False)
    Title = models.CharField(max_length=50, null = False, blank = False)

    def __str__(self):
        return self.Title



class Tag(TimeStampedModel):
    TagID = models.IntegerField
    Name = models.CharField(max_length=50, null=False, blank=False)
    Video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
