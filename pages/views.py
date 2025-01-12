from django.urls import reverse_lazy
from django.views.generic import FormView

from pages.models import PhotoSlider
from pages.forms import ContactForm
from pages.emails import send_email
from preferences.models import WebsiteOwner


class HomePageView(FormView):
    template_name = 'pages/home_page.html'
    form_class = ContactForm
    success_url = reverse_lazy('pages:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sliders'] = PhotoSlider.objects.all()
        context['owner'] = WebsiteOwner.objects.first()
        return context

    def form_valid(self, form):
        send_email(self.request, form.cleaned_data)
        return super().form_valid(form)
