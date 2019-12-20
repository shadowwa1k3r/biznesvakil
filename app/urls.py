from django.urls import path

from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('management/', ManagementListView.as_view(), name='management.list'),
]
