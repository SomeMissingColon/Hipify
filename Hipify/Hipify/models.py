from django.db import models

class Collaborator(models.Model):
    name = models.CharField(max_length=30)
    origin_story = models.TextField()

class Client(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()


class Solution(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    collaborator = models.ForeignKey(Collaborator,on_delete=models.CASCADE)

class Project(models.Model):
    collaborator = models.ForeignKey(Collaborator,on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Client, on_delete=models.CASCADE)

    name = models.CharField(max_length=30)
    description = models.TextField()
    picture = models.ImageField

