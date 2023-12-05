from django.db import models
from django.core.validators import int_list_validator
from random import shuffle
from django.contrib.auth.models import User

# Create your models here.

class Wordlist(models.Model):
    name = models.CharField(max_length=100)
    words = models.TextField()
    def __str__(self):
        return self.name

class UserWordlists(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    wordlist = models.ForeignKey(Wordlist, related_name="filter", on_delete=models.CASCADE)

class Patient (models.Model):
    first_name = models.CharField(max_length=60, name="Vorname")
    last_name = models.CharField(max_length=60, name="Nachname")
    profile_cat = models.ImageField(name="Profilbild")
    duration = models.IntegerField(default=1000)
    duration_time = models.IntegerField(default=1000, verbose_name="Anzeigedauer (in ms)")
    therapist = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.Vorname + " " + self.Nachname
    
class Test(models.Model):
    wordlist = Wordlist
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    duration = models.IntegerField(default=1000)
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
    def __str__(self):
        return self.wordlist + " " + self.patient