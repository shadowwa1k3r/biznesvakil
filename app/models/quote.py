from django.db import models


class Quote(models.Model):
    author_name_ru = models.TextField()
    author_name_uz = models.TextField()
    author_name_en = models.TextField()
    position_ru = models.TextField()
    position_uz = models.TextField()
    position_en = models.TextField()
    content_ru = models.TextField()
    content_uz = models.TextField()
    content_en = models.TextField()
    image = models.ImageField()

    class Meta:
        db_table = 'quotes'

    def __str__(self):
        return self.author_name_ru