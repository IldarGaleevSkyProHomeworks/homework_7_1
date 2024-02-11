from django.db import models

from utils.hash_storage import HashStorage, course_preview_images


class NamedItemMixin(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='Название'
    )

    description = models.TextField(
        max_length=1024,
        verbose_name='Описание'
    )

    class Meta:
        abstract = True


class HasPreviewMixin(models.Model):
    preview = models.ImageField(
        upload_to=course_preview_images,
        storage=HashStorage(),
        null=True,
        blank=True,
        verbose_name='Превью',
    )

    class Meta:
        abstract = True


class Course(NamedItemMixin, HasPreviewMixin, models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(NamedItemMixin, HasPreviewMixin, models.Model):
    video_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Ссылка на видео'
    )

    courses = models.ManyToManyField(
        Course,
        related_name='lessons',
        verbose_name='Включен в курсы'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
