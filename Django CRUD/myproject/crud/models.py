from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.CharField(max_length=40)
    sname = models.CharField(max_length=255)
    scontact = models.CharField(max_length=150)

    def __str__(self):
        return self.sname

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject
