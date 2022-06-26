from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class note(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=800)
    create = models.DateTimeField(auto_now_add=True)
    
    def total(self):
        return self.title.count()