from django.db import models


class Numbers(models.Model):
    title_ru = models.TextField()
    description_ru = models.TextField()
    title_uz = models.TextField()
    description_uz = models.TextField()
    title_en = models.TextField()
    description_en = models.TextField()
    element1_title_ru = models.TextField()
    element1_title_uz = models.TextField()
    element1_title_en = models.TextField()
    element1_value = models.TextField()
    element2_title_ru = models.TextField()
    element2_title_uz = models.TextField()
    element2_title_en = models.TextField()
    element2_value = models.TextField()
    element3_title_ru = models.TextField()
    element3_title_uz = models.TextField()
    element3_title_en = models.TextField()
    element3_value = models.TextField()
    element4_title_ru = models.TextField()
    element4_title_uz = models.TextField()
    element4_title_en = models.TextField()
    element4_value = models.TextField()

    class Meta:
        db_table = 'numbers'

    def __str__(self):
        return self.title_ru