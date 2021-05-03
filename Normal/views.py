from django.views.generic import TemplateView
from Super.models import Infos, Team
from collections import defaultdict

class RankingView(TemplateView):
    template_name = 'ranking.html'

    def get(self, request, *args, **kwargs):
        check = defaultdict(int) # 점수보드
        infos = Infos.objects.values()
        teams = Team.objects.values()

        for info in infos :
            check[info['team']] += (info['lec_check']+info['att_check']+info['ass_check']).count('Y')

        for team in teams :
            check[team['first']] += 3
            check[team['second']] += 2
            check[team['third']] += 1

        ranking = [ [score,team_name] for (team_name, score) in check.items() ]
        ranking.sort(reverse=True)

        ctx = {"ranking":ranking}
        return self.render_to_response(ctx)