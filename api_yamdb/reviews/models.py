from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
    RegexValidator
)
from django.db import models


class User(AbstractUser):
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLES = (
        (ADMIN, 'Administrator'),
        (MODERATOR, 'Moderator'),
        (USER, 'User'),
    )

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=254,
        unique=True,
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        null=True,
        unique=True,
        #validators=(
        #    RegexValidator(
        #        regex=r'^[\w.@+-]+\z)',
        #        message='Используйте только буквы, цифры и символы:@/./+/-/_'
        #    ),
        #)
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=50,
        choices=ROLES,
        default=USER
    )
    bio = models.TextField(
        verbose_name='О себе',
        null=True,
        blank=True
    )

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = (
            models.CheckConstraint(
                check=~models.Q(username__iexact="me"),
                name="username_is_not_me"
            ),
            models.UniqueConstraint(
                name='username_email_unique',
                fields=('username', 'email')
            ),
        )


class Categories(models.Model):
    name = models.CharField(
        verbose_name='Наименование категории',
        max_length=256,
        db_index=True,
    )
    slug = models.SlugField(
        verbose_name='Ссылка',
        unique=True,
        max_length=50,
        validators=(
            RegexValidator(
                regex='^[-a-zA-Z0-9_]+$',
                message='Используйте только буквы, цифры и символ "_"'
            ),
        )
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.TextField(
        verbose_name='Наименование категории',
        max_length=256,
        db_index=True,
    )
    slug = models.SlugField(
        verbose_name='Ссылка',
        unique=True,
        max_length=50,
        validators=(
            RegexValidator(
                regex='^[-a-zA-Z0-9_]+$',
                message='Используйте только буквы, цифры и символ "_"'
            ),
        )
    )

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        verbose_name='Имя произведения',
        max_length=250,
        db_index=True,)
    year = models.IntegerField(
        verbose_name='Год',
        db_index=True,
        validators=(
            MinValueValidator(
                1701,
                message='Мы собираем отзывы на произведения от XVIII века'
            ),
            MaxValueValidator(
                datetime.now().year,
                message='Год не может быть из будущего'
            ),
        )
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    genre = models.ManyToManyField(
        Genres,
        verbose_name='Жанр',
        related_name='titles',
        db_index=True,
    )
    category = models.ForeignKey(
        Categories,
        verbose_name='Категория',
        related_name='titles',
        null=True,
        on_delete=models.SET_NULL,
        db_index=True,
    )

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField(
        verbose_name='Текст',
        db_index=True,
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор отзыва',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(
        verbose_name='Оценка',
        validators=(
            MinValueValidator(0, message='Оценка не может быть меньше 0'),
            MaxValueValidator(10, message='Оценка не может быть больше 10'),
        )
    )
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        constraints = (
            models.UniqueConstraint(
                name='review_unique',
                fields=('author', 'title',)
            ),
        )
        ordering = ('-pub_date',)


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Комментарий',
        db_index=True,
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    review = models.ForeignKey(
        Review,
        verbose_name='Отзыв',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)
