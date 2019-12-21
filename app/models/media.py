from django.db import models


class Photo(models.Model):
    title_ru = models.TextField()
    title_uz = models.TextField()
    title_en = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    file = models.ImageField(upload_to='gallery/photo/')

    class Meta:
        db_table = 'photos'

    def __str__(self):
        return self.title_ru


class Video(models.Model):
    title_ru = models.TextField()
    title_uz = models.TextField()
    title_en = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='gallery/video/')
    video = models.FileField(upload_to='gallery/video/')

    class Meta:
        db_table = 'videos'

    def __str__(self):
        return self.title_ru