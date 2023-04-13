from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    """Тег"""
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Название тега'
    )
    slug = models.SlugField(
        max_length=30,
        unique=True,
        verbose_name='Адрес тега'
    )


class Poem(models.Model):
    """Модель стихотворения"""
    name = models.CharField(
        max_length=200,
        verbose_name='Название стихотворения'
    )
    text = models.CharField(
        max_length=10000000,
        verbose_name='Стихотворение'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='poems',
        verbose_name='Автор стихотворения'
    )
    tags = models.ManyToManyField(
        Tag,
        related_name='poems',
        verbose_name='Теги'
    )


class Comment(models.Model):
    """Модель комментария"""
    text = models.CharField(
        max_length=1000,
        verbose_name='Текст комментария'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время публикации'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    poem = models.ForeignKey(
        Poem,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Стихотворение'
    )
