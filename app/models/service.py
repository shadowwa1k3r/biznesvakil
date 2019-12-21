from django.db import models

class Service(models.Model):
    title_en = models.TextField()
    title_ru = models.TextField()
    title_uz = models.TextField()
    description_en = models.TextField()
    description_ru = models.TextField()
    description_uz = models.TextField()
    image = models.ImageField(upload_to='services/')
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'services'

    def __str__(self):
        return self.title_ru