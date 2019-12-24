from django.db import models


class Ticker(models.Model):
    name_ru = models.TextField(null=True, blank=True)
    name_uz = models.TextField(null=True, blank=True)
    name_en = models.TextField(null=True, blank=True)
    title_ru = models.TextField()
    title_uz = models.TextField()
    title_en = models.TextField()
    content_ru = models.TextField()
    content_en = models.TextField()
    content_uz = models.TextField()

    class Meta:
        db_table = 'tickers'

    def __str__(self):
        return self.title_ru