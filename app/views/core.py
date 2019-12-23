from django.views.generic import View, ListView, TemplateView
from django.shortcuts import render

from app.models import News, MapData, City, Photo, Video, About, Numbers
from app.models.service import Service
from django.utils.translation import get_language


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = get_language()
        print(lang)
        city_list = City.objects.all()
        cities = {}
        for city in city_list:
            subdict = {}
            if lang=='ru':
                subdict['name'] = city.name_ru
                subdict['content'] = city.mapdata_set.all()[0].content_ru
            elif lang=='uz':
                subdict['name'] = city.name_uz
                subdict['content'] = city.mapdata_set.all()[0].content_uz
            elif lang=='en':
                subdict['name'] = city.name_en
                subdict['content'] = city.mapdata_set.all()[0].content_en


            cities[city.code] = subdict

        # cities = {
        #     'UZ-AN': 'Ўзбекистон Республикаси Президенти ҳузуридаги Тадбиркорлик субъектларининг хуқуқлари ва қонуний манфаатларини ҳимоя қилиш бўйича вакил девонининг Андижон вилоятида фаолият кўрсатувчи ходимлар 170131, Андижон вилояти, Андижон шаҳри, Миллий тикланиш кўчаси, 24 Тел: (74) 228-29-66',
        #     'UZ-BU': regions['bukhara'][lang]
        # }

        news = News.objects.all().order_by('created')[:5]
        context['header_news'] = news[0:2]
        context['footer_news'] = news[2:5]
        context['services'] = Service.objects.all()
        context['map_datas'] = cities
        if About.objects.all().count()>0:
            context['about'] = About.objects.all().first()
        context['photos'] = Photo.objects.all().order_by('created')[:4]
        context['video'] = Video.objects.all().order_by('created')[:2]
        context['numbers'] = Numbers.objects.all().first()

        return context