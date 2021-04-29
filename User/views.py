from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        ctx = {'user':request.session.get('user')}
        return self.render_to_response(ctx)
