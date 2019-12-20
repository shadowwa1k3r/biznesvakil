from django.db import models


class Management(models.Model):
    full_name_ru = models.CharField(max_length=255)
    full_name_uz = models.CharField(max_length=255)
    full_name_en = models.CharField(max_length=255)
    position_ru = models.CharField(max_length=255)
    position_uz = models.CharField(max_length=255)
    position_en = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    photo = models.ImageField()
    email = models.CharField(max_length=255)
    receive_days_ru = models.CharField(max_length=255)
    receive_days_uz = models.CharField(max_length=255)
    receive_days_en = models.CharField(max_length=255)

    class Meta:
        db_table = 'management'

    def __str__(self):
        return self.full_name_uz
