from django.db import models


class DeviceSignals(models.Model):
    code = models.CharField(max_length=2000)

    price = models.DecimalField(max_digits=9, decimal_places=2)

    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


class TelegramUsers(models.Model):
    telegram_id = models.IntegerField(verbose_name='ИД пользователя в телеграм')

    total_sum = models.DecimalField(verbose_name='Общая сумма баллов', max_digits=9, decimal_places=2)

    def __str__(self):
        return f'Пользователь {self.telegram_id}'
