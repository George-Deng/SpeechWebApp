#ORM file that describes UploadPrediction table in database
from django.db import models
from upload.models import Upload
from django.db.models.deletion import CASCADE


class UploadPrediction(models.Model):
    gender_prediction = models.CharField(max_length=20, blank=True, null=True)
    upload = models.ForeignKey(Upload, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
