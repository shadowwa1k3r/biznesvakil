from django.db import models


class Menu(models.Model):
    name_ru = models.TextField()
    name_uz = models.TextField()
    name_en = models.TextField()
    parent = models.ForeignKey(to='Menu', on_delete=models.CASCADE,related_name='s_menu', null=True, blank=True)
    page_alias = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'menu'

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


class Page(models.Model):
    content_ru = models.TextField()
    content_uz = models.TextField()
    content_en = models.TextField()
    menu = models.OneToOneField(Menu, on_delete=models.CASCADE, related_name='menu')
    created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'page'

    def __str__(self):
        return self.content_ru
