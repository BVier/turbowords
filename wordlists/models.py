from django.db import models
from django.core.validators import int_list_validator
from random import shuffle

# Create your models here.

class Wordlist(models.Model):
    name = models.CharField(max_length=100, default="Liste")
    words = models.TextField()
    duration = models.IntegerField()
    def __str__(self):
        return self.name

class Test(models.Model):
    wordlist = Wordlist
    participant = models.CharField(max_length=60)
    duration = models.IntegerField()
    completed = models.BooleanField(default= False)
    word_count = models.IntegerField(default=0)
    correct_count = models.IntegerField(default=0)
    shuffled_words = models.TextField()
    def next_word(self):
        word = self.shuffled_words.splitlines()[self.word_count]
        self.word_count +=1
        self.save()
        return word
    def finished(self):
        return self.word_count >= len(self.shuffled_words.splitlines())