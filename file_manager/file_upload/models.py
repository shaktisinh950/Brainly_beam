import os
from django.db import models

def upload_to(instance, filename):
    ext = filename.split('.')[-1].lower()
    if ext == 'pdf':
        return os.path.join('pdf', filename)
    elif ext == 'docx':
        return os.path.join('doc', filename)
    elif ext in ['jpg', 'png']:
        return os.path.join('images', filename)
    return filename

class UploadedFile(models.Model):
    file = models.FileField(upload_to=upload_to)
    uploaded_at = models.DateTimeField(auto_now_add=True)
