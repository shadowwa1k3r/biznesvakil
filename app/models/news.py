from django.db import models


class News(models.Model):
    title_ru = models.CharField(max_length=255)
    title_uz = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    content_ru = models.TextField()
    content_uz = models.TextField()
    content_en = models.TextField()
    image = models.ImageField(upload_to='news/')
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'news'

    def __str__(self):
        return self.title_ru


class NewsFiles(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/')

    class Meta:
        db_table = 'news_files'

    def __str__(self):
        return self.news.title_ru
