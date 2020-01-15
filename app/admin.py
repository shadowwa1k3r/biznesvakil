from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


class PageAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(Management)
admin.site.register(News)
admin.site.register(Service)
admin.site.register(NewsFiles)
admin.site.register(City)
admin.site.register(MapData, PageAdmin)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(About)
admin.site.register(Numbers)
admin.site.register(Ticker)
admin.site.register(Quote)
admin.site.register(Menu)
admin.site.register(Feedback)
admin.site.register(Ally)
admin.site.register(Footer)
admin.site.register(Page, PageAdmin)
admin.site.register(MapDefault, PageAdmin)