from django.http.response import HttpResponse
from django.urls import reverse
from django.views.generic import View, ListView, TemplateView
from django.shortcuts import render, redirect
import json
from requests.auth import HTTPBasicAuth
import requests
from app.models import News, MapData, City, Photo, Video, About, Numbers, Page, MapDefault, Ally, Footer, SideBanner
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
        map_default = ''
        for city in city_list:
            subdict = {}
            if lang=='ru':
                subdict['name'] = city.name_ru
                if len(city.mapdata_set.all()) == 0:
                    subdict['content'] = ''
                else:
                    subdict['content'] = city.mapdata_set.all()[0].content_ru
                if MapDefault.objects.all().count() > 0:
                    map_default = MapDefault.objects.first().content_ru
            elif lang == 'uz':
                subdict['name'] = city.name_uz
                if len(city.mapdata_set.all()) == 0:
                    subdict['content'] = ''
                else:
                    subdict['content'] = city.mapdata_set.all()[0].content_uz
                if MapDefault.objects.all().count() > 0:
                    map_default = MapDefault.objects.first().content_uz
            elif lang == 'en':
                subdict['name'] = city.name_en
                if len(city.mapdata_set.all()) == 0:
                    subdict['content'] = ''
                else:
                    subdict['content'] = city.mapdata_set.all()[0].content_en
                if MapDefault.objects.all().count() > 0:
                    map_default = MapDefault.objects.first().content_en


            cities[city.code] = subdict

        # cities = {
        #     'UZ-AN': 'Ўзбекистон Республикаси Президенти ҳузуридаги Тадбиркорлик субъектларининг хуқуқлари ва қонуний манфаатларини ҳимоя қилиш бўйича вакил девонининг Андижон вилоятида фаолият кўрсатувчи ходимлар 170131, Андижон вилояти, Андижон шаҳри, Миллий тикланиш кўчаси, 24 Тел: (74) 228-29-66',
        #     'UZ-BU': regions['bukhara'][lang]
        # }

        news = News.objects.all().order_by('-created')[:5]
        context['header_news'] = news[0:2]
        context['footer_news'] = news[2:5]
        context['services'] = Service.objects.all()
        context['map_datas'] = cities
        context['map_default'] = map_default
        context['allies'] = Ally.objects.all()

        if About.objects.all().count()>0:
            context['about'] = About.objects.all().first()
        context['photos'] = Photo.objects.all().order_by('-created')[:4]
        context['video'] = Video.objects.all().order_by('-created')[:2]
        context['numbers'] = Numbers.objects.all().first()
        context['numbers'] = Numbers.objects.all().first()
        context['banners'] = SideBanner.objects.all()[:2]

        return context


class MenuView(TemplateView):
    template_name = 'static.html'

    def get(self, request, *args, **kwargs):
        if self.kwargs['page_alias'] == 'management':
            return redirect(reverse('management.list'))
        if self.kwargs['page_alias'] == 'news':
            return redirect(reverse('news.list'))
        if self.kwargs['page_alias'] == 'photo-gallery':
            return redirect(reverse('gallery.list.photo'))
        if self.kwargs['page_alias'] == 'video-gallery':
            return redirect(reverse('gallery.list.video'))
        if self.kwargs['page_alias'] == 'feedback':
            return redirect(reverse('feedback'))
        return super(MenuView, self).get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        page = Page.objects.get(menu__page_alias=self.kwargs['page_alias'])
        context['page'] = page
        return context

class InspectorCheckView(View):
    def post(self, request):
        uid = self.request.POST.get('uid')
        r = requests.get(f'http://tt.biznesvakil.uz/api/external/verification/{uid}', auth=HTTPBasicAuth('bo_inn_api', 'Qwerty123$'))
        return HttpResponse(r.json(), content_type='application/json')