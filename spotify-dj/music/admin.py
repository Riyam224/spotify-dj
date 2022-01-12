from django.contrib import admin

# Register your models here.
from .models import Music , Album

admin.site.register(Music)
admin.site.register(Album)