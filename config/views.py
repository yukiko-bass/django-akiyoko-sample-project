from django.views.generic import TemplateView
from django.contrib.auth.models import User


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_count'] = User.objects.all().count()
        return context


index = IndexView.as_view()
