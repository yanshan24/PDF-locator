from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

def uuid_hex():
    return uuid.uuid4().hex

class Author(AbstractUser):
    # model for author
    email = models.EmailField(max_length=60, unique=True)
    is_manager = models.BooleanField(default=False)
    authorID = models.CharField(unique=True, default=uuid_hex, editable=False, max_length=40)

    # USERNAME_FIELD = 'email' # use email to login
    # REQUIRED_FIELDS = ['username']

    # def get_id(self):
    #     return settings.HOST_URL + "user/" + self.authorID

    # def get_host(self):
    #     return settings.HOST_URL

    # def get_type(self):
    #     return "author"