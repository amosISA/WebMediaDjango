from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Video(models.Model):
    VideoID = models.IntegerField
    Path = models.CharField(max_length=100, null = False, blank = False)
    Title = models.CharField(max_length=50, null = False, blank = False)

    def __str__(self):
        return self.Title



class Tag(models.Model):
    TagID = models.IntegerField
    Name = models.CharField(max_length=50, null=False, blank=False)
    Video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name
