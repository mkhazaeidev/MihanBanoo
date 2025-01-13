from django.urls import reverse_lazy
from django.views.generic import FormView

from pages.models import PhotoSlider, AboutUs, Services
from pages.forms import ContactForm
from pages.emails import send_email
from preferences.models import WebsiteOwner, Titles


class HomePageView(FormView):
    template_name = 'pages/home_page.html'
    form_class = ContactForm
    success_url = reverse_lazy('pages:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['sliders'] = PhotoSlider.objects.all()
        except:
            context['sliders'] = False

        try:
            context['owner'] = WebsiteOwner.objects.first()
        except:
            context['owner'] = False

        try:
            context['about_details'] = AboutUs.objects.first()
        except:
            context['about_details'] = False

        try:
            context['services_details'] = Services.objects.all()
        except:
            context['services_details'] = list()

        try:
            context['about_titles'] = Titles.objects.get(section='about')
        except:
            context['about_titles'] = False

        try:
            context['services_titles'] = Titles.objects.get(section='services')
        except:
            context['services_titles'] = False

        try:
            context['contact_titles'] = Titles.objects.get(section='contact')
        except:
            context['contact_titles'] = False

        try:
            context['footer_titles'] = Titles.objects.get(section='footer')
        except:
            context['footer_titles'] = False

        return context

    def form_valid(self, form):
        send_email(self.request, form.cleaned_data)
        return super().form_valid(form)
