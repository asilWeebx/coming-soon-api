# your_app_name/models.py
from django.db import models

class UserEmail(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
