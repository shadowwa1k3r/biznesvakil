from django.db import models


class About(models.Model):
    header_uz = models.TextField()
    header_ru = models.TextField()
    header_en = models.TextField()
    title_uz = models.TextField()
    title_ru = models.TextField()
    title_en = models.TextField()
    content_ru = models.TextField()
    content_en = models.TextField()
    content_uz = models.TextField()

    class Meta:
        db_table = 'about'

    def __str__(self):
        return self.title_ru
