from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .models import Infos, Team
from .forms import InfoForm, TeamForm
from django.utils.decorators import method_decorator
from User.decorators import adminRequired

users = {"을지로" : ["강0","재0","훈0"], "강남" : ["강1","재1","훈1"], "왕십리" : ["강2","재2","훈2"]  }

class ChoiceView(TemplateView):
    template_name = 'choice.html'

    def get(self, request, *args, **kwargs):
        ctx = {"teams":users}
        return self.render_to_response(ctx)

@method_decorator(adminRequired, name = 'dispatch')
class InfoView(FormView):
    template_name = 'info.html'
    form_class = InfoForm
    success_url = '/super/choice'

    def get_initial(self) :
        initial = super().get_initial()
        team_name = self.kwargs['team_name']
        initial['team'] = team_name
        initial['name'] = users[team_name][0]

        return initial

    def form_valid(self, form):
        info = Infos(
            week = form.data.get('week'),
            name = form.data.get('name'),
            team = form.data.get('team'),
            lec_check = form.data.get('lec_check'),
            att_check = form.data.get('att_check'),
            ass_check = form.data.get('att_check')
        )
        info.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_name'] = self.kwargs['team_name']
        return context


@method_decorator(adminRequired, name = 'dispatch')
class TeamView(FormView):
    template_name = 'team.html'
    form_class = TeamForm
    success_url = '/'

    def form_valid(self, form):

        team = Team(
            week = form.data.get('week'),
            first = form.data.get('first'),
            second = form.data.get('second'),
            third = form.data.get('third')
        )
        team.save()

        return super().form_valid(form)
