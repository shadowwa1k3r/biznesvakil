from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Menu(models.Model):
    order = models.IntegerField()
    name_ru = models.TextField()
    name_uz = models.TextField()
    name_en = models.TextField()
    parent = models.ForeignKey(to='Menu', on_delete=models.CASCADE,related_name='s_menu', null=True, blank=True)
    page_alias = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'menu'
        ordering = ('order',)

    def __str__(self):
        return self.name_ru

    def has_child(self):
        if self.s_menu.all().count()>0:
            return True
        return False

    def has_parent(self):
        if self.parent:
            return True
        return False

    def has_alias_without_child(self):
        if self.s_menu.all().count() == 0 and len(self.page_alias) > 0:
            return True
        return False


@receiver(post_save, sender=Menu)
def create_menu_page(sender, instance, created, **kwargs):
    if created:
        if instance.parent:
            page = Page.objects.create(menu=instance, content_en=' ', content_uz=' ', content_ru=' ',)
            page.save()


class Page(models.Model):
    content_ru = models.TextField(null=True, blank=True)
    content_uz = models.TextField(null=True, blank=True)
    content_en = models.TextField(null=True, blank=True)
    menu = models.OneToOneField(Menu, on_delete=models.CASCADE, related_name='menu')
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'page'

    def __str__(self):
        return self.menu.name_ru
