from django.views.generic import TemplateView


class HomePageView(TemplateView):

    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['test'] = Test.objects.all()[:5]
        return context
