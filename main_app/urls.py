from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),

    # Character Routes
    path('characters/', views.CharacterList.as_view(), name="character_list"),
    path('characters/new/', views.CharacterCreate.as_view(), name="character_create"),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name="character_detail"),
    path('characters/<int:pk>/update', views.CharacterUpdate.as_view(), name="character_update"),
    path('characters/<int:pk>/delete', views.CharacterDelete.as_view(), name="character_delete"),
    path('characters/<int:pk>/powers/new/', views.PowerCreate.as_view(), name="power_create"),
]
