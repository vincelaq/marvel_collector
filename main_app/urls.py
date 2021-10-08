from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),

    # Character Routes
    path('characters/', views.CharacterList.as_view(), name="character_list"),
    path('characters/new/', views.CharacterCreate.as_view(), name="character_create"),
    path('characters/<int:pk>/', views.character_detail, name="character_detail"),
    path('characters/<int:pk>/update', views.CharacterUpdate.as_view(), name="character_update"),
    path('characters/<int:pk>/delete', views.CharacterDelete.as_view(), name="character_delete"),
    path('characters/<int:pk>/powers/new/', views.PowerCreate.as_view(), name="power_create"),

    # Team Routes
    path('teams/', views.TeamList.as_view(), name="team_list"),
    path('teams/new/', views.TeamCreate.as_view(), name="team_create"),
    path('teams/<int:pk>/', views.TeamDetail.as_view(), name="team_detail"),
    path('teams/<int:pk>/update', views.TeamUpdate.as_view(), name="team_update"),
    path('teams/<int:pk>/delete', views.TeamDelete.as_view(), name="team_delete"),
    path('teams/<int:pk>/characters/<int:character_pk>/', views.TeamCharacterAssoc.as_view(), name="team_character_assoc"),
]
