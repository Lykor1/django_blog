from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250, verbose_name='Название')
    slug = models.SlugField(max_length=250, verbose_name='Слаг')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Автор')
    body = models.TextField(verbose_name='Тело')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
