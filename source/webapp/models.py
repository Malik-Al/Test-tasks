from django.contrib.auth.models import User
from django.db import models


USER_GENDER_CHOICES = 'gender'
GENDER_CHOICES = (
    (USER_GENDER_CHOICES, 'Пол'),
    ('girl', 'Мужской'),
    ('men', 'Женский')
)


USER_COUNTRY_CHOICES = 'country'
COUNTRY_CHOICES = (
    (USER_COUNTRY_CHOICES, 'Страна'),
    ('Belarus', 'Беларусь'),
    ('Brazil', 'Бразилия'),
    ('United Kingdom', 'Великобритания'),
    ('Russia', 'Россия'),
    ('Kyrgyzstan', 'Киргизия')
)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    second_name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Отчество')
    gender = models.CharField(max_length=20, verbose_name='Пол',
                              choices=GENDER_CHOICES, default=USER_GENDER_CHOICES)
    country = models.CharField(max_length=20, verbose_name='Страна',
                               choices=COUNTRY_CHOICES, default=USER_COUNTRY_CHOICES)

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'



