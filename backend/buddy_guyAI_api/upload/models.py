
import csv
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from buddy_guyAI_api.storage_backends import PublicMediaStorage
from users.models import Patient


class Upload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient,on_delete=CASCADE, null=True)
    file = models.FileField(storage=PublicMediaStorage())
    
    def __str__(self):
        return str(self.file) +"_" +str(self.id)

class Annotation(models.Model):
    upload = models.ForeignKey(Upload, on_delete=CASCADE)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
    annotation = models.TextField()