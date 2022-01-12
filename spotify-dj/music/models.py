from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.shortcuts import reverse


from .helpers import get_audio_length
from .validators import validate_is_audio

class Music(models.Model):
    title = models.CharField(_("title"), max_length=50)
    artist = models.CharField(_("artist"), max_length=50)
    album = models.ForeignKey("Album", on_delete=models.SET_NULL , blank=True , null=True)
    time_length = models.DecimalField(_("time length"), max_digits=20, decimal_places=2)
    audio_file = models.FileField(upload_to="musics",  validators=[validate_is_audio] , blank=True , null=True)
    cover_image = models.ImageField(_("cover image "), upload_to="covers", blank=True , null=True)
    slug  = models.SlugField(blank=True , null=True)

    class Meta:
        verbose_name = _("Musoc")
        verbose_name_plural = _("Musocs")


    def __str__(self):
        return self.title

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super(Music , self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if not self.time_length:

            audio_length=get_audio_length(self.audio_file)
            self.time_length =f'{audio_length:.2f}'
        return super().save(*args, **kwargs)

    






class Album(models.Model):
    name = models.CharField(_("album"), max_length=50)

    

    class Meta:
        verbose_name = _("Album")
        verbose_name_plural = _("Albums")

    def __str__(self):
        return self.name
