from django.views.generic import TemplateView

class HomePageView(TemplateView):
  template_name = 'pages/home.html'


class AboutUsView(TemplateView):
 template_name = 'pages/About_us.html'