from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

def uuid_hex():
    return uuid.uuid4().hex

class Author(AbstractUser):
    email = models.EmailField(max_length=60, unique=True)
    is_manager = models.BooleanField(default=False)
    authorID = models.CharField(unique=True, default=uuid_hex, editable=False, max_length=40)

class HistoryItem(models.Model):
    pdf_file = models.TextField(blank=True)
    file_name = models.CharField(default = 'pdfname.pdf', max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    authorID = models.CharField(max_length=40, default=uuid_hex)
    json_data = models.TextField(blank=True)

    def __str__(self):
        return self.file_name