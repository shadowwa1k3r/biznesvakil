from .core import IndexView, MenuView
from .management import ManagementListView
from .news import NewsListView, NewsDetailView
from .gallery import GalleryView, VideoGalleryView
from .feedback import FeedbackAPIView

__all__ = [
    'IndexView',
    'ManagementListView',
    'NewsListView',
    'NewsDetailView',
    'GalleryView',
    'VideoGalleryView',
    'MenuView',
    'FeedbackAPIView'
]
