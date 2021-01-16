from django.db import models

class Voice(models.Model):
    username = models.CharField(default="", max_length=40,blank=False,null=False)
    voice = models.FileField(blank=True, upload_to='sounds/')
