from django.urls import path

from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('management/', ManagementListView.as_view(), name='management.list'),
    path('news/', NewsListView.as_view(), name='news.list'),
    path('gallery/photo/', GalleryView.as_view(), name='gallery.list.photo'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news.detail'),
    path('gallery/video/', VideoGalleryView.as_view(), name='gallery.list.video'),
]
