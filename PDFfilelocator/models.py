from django.db import models
import uuid

def uuid_hex():
    return uuid.uuid4().hex

class User(models.Model):
    # model for 
    email = models.EmailField(max_length=60, unique=True)
    password = models.CharField(max_length=50)
    is_manager = models.BooleanField(default=False)

    # USERNAME_FIELD = 'email' # use email to login
    # REQUIRED_FIELDS = ['username']

    # def get_id(self):
    #     return settings.HOST_URL + "user/" + self.authorID

    # def get_host(self):
    #     return settings.HOST_URL

    # def get_type(self):
    #     return "author"