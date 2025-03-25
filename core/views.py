from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib import messages

# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        duration = request.POST.get('duration', 3)
        transition = request.POST.get('transition', 'fade')

        if not images:
            messages.error(request, 'Please select at least one image.')
            return self.get(request, *args, **kwargs)

        # Here you would implement the image to video conversion logic
        # For now, we'll just show a success message
        messages.success(request, 'Video creation started! We\'ll notify you when it\'s ready.')
        return self.get(request, *args, **kwargs)
