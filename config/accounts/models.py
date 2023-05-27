from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ["-id"]
