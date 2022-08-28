from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserUploadModel(models.Model):
    
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    file = models.FileField(upload_to = 'file_uploads/%d%m%Y')
    