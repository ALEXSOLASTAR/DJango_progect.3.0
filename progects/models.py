from django.core.exceptions import ValidationError
from django.db import models

from languages.models import program_language


class Progect(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Назва проекту')
    progect_progres = models.PositiveSmallIntegerField(verbose_name='Погрес проекту')
    from_language = models.ForeignKey(program_language, on_delete=models.CASCADE,
                                      related_name='from_language_set',
                                      verbose_name='З якої мови'
                                      )
    to_language = models.ForeignKey(program_language, on_delete=models.CASCADE,
                                      related_name='to_language_set',
                                      verbose_name='До якої мови'
                                      )

    def __str__(self):
        return f"Проект {self.name} на {self.from_language}"

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекти'
        ordering = ['from_language']

    def clean(self):
        if self.from_language == self.to_language:
            raise ValidationError('Змініть мову на яку переноситься проект')
        qs = Progect.objects.filter(from_language=self.from_language,
                                    to_language=self.to_language,
                                    progect_progres=self.progect_progres
                                    ).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Змініть мову на яку переноситься проект')


    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
