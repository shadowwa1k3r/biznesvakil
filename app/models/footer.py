from django.db import models


class Footer(models.Model):
    content1_ru = models.TextField(null=True, blank=True)
    content1_uz = models.TextField(null=True, blank=True)
    content1_en = models.TextField(null=True, blank=True)
    facebook = models.TextField(null=True, blank=True)
    instagram = models.TextField(null=True, blank=True)
    twitter = models.TextField(null=True, blank=True)
    telegram = models.TextField(null=True, blank=True)
    youtube = models.TextField(null=True, blank=True)
    address_ru = models.TextField(null=True, blank=True)
    address_en = models.TextField(null=True, blank=True)
    address_uz = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    mail = models.TextField(null=True, blank=True)
    header_title_ru = models.TextField(null=True, blank=True)
    header_title_uz = models.TextField(null=True, blank=True)
    header_title_en = models.TextField(null=True, blank=True)
    social_ru = models.TextField(null=True, blank=True)
    social_uz = models.TextField(null=True, blank=True)
    social_en = models.TextField(null=True, blank=True)
    copyright_ru = models.TextField(null=True, blank=True)
    copyright_uz = models.TextField(null=True, blank=True)
    copyright_en = models.TextField(null=True, blank=True)


    class Meta:
        db_table = 'footer'

    def __str__(self):
        return self.content1_ru