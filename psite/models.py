from django.db import models


# Create your models here.
class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    resources_used = models.CharField(max_length=200)
    repo = models.CharField(max_length=100)
    cover = models.FileField()


class Subscriptions(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)


class Feedback(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    feedback = models.CharField(max_length=100)
