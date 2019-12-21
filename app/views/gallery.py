from django.views.generic import TemplateView, DetailView

from app.models import Photo, Video


class GalleryView(TemplateView):
    template_name = 'gallery.html'

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context['photos'] = Photo.objects.all()

        return context


class VideoGalleryView(TemplateView):
    template_name = 'video.html'

    def get_context_data(self, **kwargs):
        context = super(VideoGalleryView, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.all()

        return context


class GalleryDetailView(DetailView):
    model = Photo
    template_name = 'gallery_view.html'