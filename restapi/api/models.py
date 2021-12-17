from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Data (models.Model):

    oksi=models.CharField(max_length=100, blank=True)
    slug = models.SlugField(unique=True, max_length=150, editable=False, blank=True)


    def get_slug(self):
        slug = 1
        unique = slug

        return unique
   


    def __str__(self):
        return self.oksi
    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()

        self.slug = self.get_slug()
        return super(Data, self).save(*args,**kwargs)
