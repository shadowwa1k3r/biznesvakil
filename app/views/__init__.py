from .core import IndexView
from .management import ManagementListView
from .news import NewsListView, NewsDetailView
from .gallery import GalleryView, VideoGalleryView

__all__ = [
    'IndexView',
    'ManagementListView',
    'NewsListView',
    'NewsDetailView',
    'GalleryView',
    'VideoGalleryView'
]
