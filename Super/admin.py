from django.contrib import admin
from .models import Infos, Team

class InfosAdmin(admin.ModelAdmin):
    list_display = ('week', 'name', 'team','lec_check', 'att_check', 'ass_check')

admin.site.register(Infos, InfosAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('week', 'first', 'second', 'third')

admin.site.register(Team, TeamAdmin)