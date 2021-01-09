from django.views.generic import ListView, DetailView

from app.models import News


class NewsListView(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news.html'

    def get_queryset(self):
        return News.objects.all().order_by('-created')


class NewsDetailView(DetailView):
    model = News
    context_object_name = 'new'
    template_name = 'news_view.html'
