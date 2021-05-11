from django.urls import path
from .views import UserList, TeamRankingList, ScoreCreate, AddPointCreate
from rest_auth.views import ( LoginView, LogoutView, PasswordChangeView, 
PasswordResetView, PasswordResetConfirmView )
from rest_auth.registration.views import RegisterView

urlpatterns = [
    
    path('login/', LoginView.as_view(), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('registration/', RegisterView.as_view(), name='Register'),

    path('<str:team>/users/', UserList.as_view(), name='Team-User-list'),
    path('ranking/', TeamRankingList.as_view(), name='Team-Ranking-list'),
    path('score/<str:team>/', ScoreCreate.as_view(), name='Score-create'),
    path('addpoint/', AddPointCreate.as_view(), name='Add_Point-create')

]