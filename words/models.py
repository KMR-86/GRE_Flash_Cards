from django.db import models


class words(models.Model):
    word = models.TextField()
    meaning = models.TextField()
    sentence1 = models.TextField()
    sentence2 = models.TextField()
    etymology = models.TextField()
    mnemonic = models.TextField()
    hardness_level = models.IntegerField()


# Create your models here.
