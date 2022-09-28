from django.db import models

class Status(models.Model):
    name = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.name

class Train(models.Model):
    description = models.CharField(max_length = 255, blank = False, null = False,
        error_messages = {'blank': 'Description cannot be blank', 'null': 'Description cannot be null'})
    username    = models.CharField(max_length = 255, blank = False, null = False,
        error_messages = {'blank': 'User cannot be blank', 'null': 'User cannot be null'})
    status      = models.ForeignKey(Status, blank = False, null = False,
        error_messages = {'blank': 'Status cannot be blank', 'null': 'Status cannot be null'})
    departure   = models.DateTimeField('departure date', blank = False, null = False)
    arrival     = models.DateTimeField('arrival date', blank = True, null = True)

    def __unicode__(self):
        return self.description