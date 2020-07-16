from django.db import models


class words(models.Model):
    word = models.TextField()
    meaning = models.TextField()
    sentence1 = models.TextField()
    sentence2 = models.TextField()
    etymology = models.TextField()
    mnemonic = models.TextField()


def __str__(self):
    return self.word

# Create your models here.
