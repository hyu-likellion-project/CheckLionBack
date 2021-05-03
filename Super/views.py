from django.views.generic import TemplateView


users = {"을지로" : ["강0","재0","훈0"], "강남" : ["강1","재1","훈1"], "왕십리" : ["강2","재2","훈2"]  }

class ChoiceView(TemplateView):
    template_name = 'choice.html'

    def get(self, request, *args, **kwargs):
        ctx = {"teams":users}
        return self.render_to_response(ctx)