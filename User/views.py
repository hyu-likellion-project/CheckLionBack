from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from .forms import RegisterForm
from .models import Users
from django.contrib.auth.hashers import make_password

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        ctx = {'user':request.session.get('user')}
        return self.render_to_response(ctx)

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        user = Users(
            email = form.data.get('email'),
            password = make_password(form.data.get('password')),
            level = 'user'
        )
        user.save()

        return super().form_valid(form)