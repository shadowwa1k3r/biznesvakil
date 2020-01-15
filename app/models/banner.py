from django.db import models


class SideBanner(models.Model):
    title_ru = models.TextField()
    title_uz = models.TextField()
    title_en = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='banner/')

    class Meta:
        db_table = 'side_banner'

    def __str__(self):
        return self.title_ru