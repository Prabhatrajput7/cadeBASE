from django.views.generic import TemplateView

class Homepg(TemplateView):
    template_name = 'index.html'

class Thankspg(TemplateView):
    template_name = 'thanks.html'    
