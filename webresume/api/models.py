from django.db import models

class Person(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    contact = models.TextField()
    about = models.TextField()
    education = models.TextField()
    skills = models.TextField()
    work = models.TextField()
