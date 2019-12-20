from django.views.generic import ListView

from app.models import Management


class ManagementListView(ListView):
    model = Management
    template_name = 'manage.html'
    context_object_name = 'managements'
