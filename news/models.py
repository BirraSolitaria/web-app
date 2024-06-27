from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils import timezone

class Articles(models.Model):
    title = models.CharField(
        'Название',
        max_length= 50,
        validators=[
            MinLengthValidator(4, 'Название должно быть не менее 4 символов'),
            MaxLengthValidator(50, 'Название должно быть не более 50 символов')
        ]
    )
    anons = models.CharField(
        'Анонс',
        max_length=100,
        validators=[
            MaxLengthValidator(100, 'Анонс должен быть не более 100 символов')
        ]
    )
    full_text = models.TextField(
        'Статья',
        validators=[
            MinLengthValidator(50, 'Статья должна быть не менее 50 символов')
        ]
    )
    image = models.ImageField(upload_to='uploads_model/', null=True, blank=True)
    date = models.DateTimeField('Дата публикации', default=timezone.now)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
