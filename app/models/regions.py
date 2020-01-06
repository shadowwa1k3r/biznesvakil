from django.db import models


class City(models.Model):
    name_ru = models.TextField(blank=True, null=True)
    name_uz = models.TextField(blank=True, null=True)
    name_en = models.TextField(blank=True, null=True)
    code = models.TextField()

    class Meta:
        db_table = 'cities'

    def __str__(self):
        return self.name_ru


class MapData(models.Model):
    content_ru = models.TextField(blank=True, null=True)
    content_uz = models.TextField(blank=True, null=True)
    content_en = models.TextField(blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = 'map_datas'

    def __str__(self):
        return self.content_ru


class MapDefault(models.Model):
    content_ru = models.TextField(blank=True, null=True)
    content_uz = models.TextField(blank=True, null=True)
    content_en = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'map_default'

    def __str__(self):
        return self.content_ru