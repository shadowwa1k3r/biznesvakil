from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from app.models import Feedback


class FeedbackAPIView(View):
    def get(self, request):
        return render(request, 'feedback.html')

    def post(self, request):
        fname = request.POST.get('name')
        mail = request.POST.get('pochta')
        phone = request.POST.get('phone')
        comment = request.POST.get('message')
        Feedback.objects.create(full_name=fname, email=mail, phone=phone, comment=comment)
        return render(request, 'feedback.html', {'status': 'True'})