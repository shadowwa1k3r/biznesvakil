from app.views.core import InspectorCheckView
from django.urls import path

from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('menu/<str:page_alias>/', MenuView.as_view(), name='menu'),
    path('management/', ManagementListView.as_view(), name='management.list'),
    path('news/', NewsListView.as_view(), name='news.list'),
    path('gallery/photo/', GalleryView.as_view(), name='gallery.list.photo'),
    path('news/<int:pk>', NewsDetailView.as_view(), name='news.detail'),
    path('feedback/', FeedbackAPIView.as_view(), name='feedback'),
    path('gallery/video/', VideoGalleryView.as_view(), name='gallery.list.video'),
    path('inspector/', InspectorCheckView.as_view(), name='inspector.check')
]
