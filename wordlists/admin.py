from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Wordlist)
admin.site.register(Patient)
admin.site.register(Test)
admin.site.register(UserWordlists)