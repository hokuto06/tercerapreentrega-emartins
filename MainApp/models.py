from django.db import models

class AccessPoints(models.Model):

    deviceName = models.CharField(max_length=30)
    ipAddress = models.GenericIPAddressField()
    status = models.IntegerField()


