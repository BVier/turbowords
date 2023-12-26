from django.db import models
from django.core.validators import int_list_validator
from random import shuffle
from django.contrib.auth.models import User

# Create your models here.

class Wordlist(models.Model):
    name = models.CharField(max_length=100, default="Liste")
    words = models.TextField()
    duration = models.IntegerField(default=1000)
    def __str__(self):
        return self.name

class Test(models.Model):
    wordlist = Wordlist
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

class UserWordlists(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wordlist = models.ForeignKey(Wordlist, related_name="filter", on_delete=models.CASCADE)
