"""CheckLionBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from User.views import HomeView, RegisterView, LoginView, logout
from Super.views import ChoiceView, InfoView, TeamView
from Normal.views import RankingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('user/register/', RegisterView.as_view()),
    path('user/login/', LoginView.as_view()),
    path('user/logout/', logout),
    path('super/choice/', ChoiceView.as_view()),
    path('super/info/<str:team_name>', InfoView.as_view()),
    path('super/team/', TeamView.as_view()),
    path('normal/ranking/', RankingView.as_view()),
]
