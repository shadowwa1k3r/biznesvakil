from django.db import models


class Ally(models.Model):
    name_ru = models.TextField()
    name_uz = models.TextField()
    name_en = models.TextField()
    image = models.ImageField(upload_to='ally/')
    link = models.TextField(default='')

    class Meta:
        db_table = 'allies'

    def __str__(self):
        return self.name_ru