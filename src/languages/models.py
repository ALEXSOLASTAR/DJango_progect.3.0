from django.db import models
from pyexpat import model

from django.urls import reverse


class program_language(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Мова')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Мова'
        verbose_name_plural = 'Мови'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('languages:detail', kwargs={'pk': self.pk})
