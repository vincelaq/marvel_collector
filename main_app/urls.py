from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),

    # Character Routes
    path('characters/', views.CharacterList.as_view(), name="character_list"),
    path('characters/new/', views.CharacterCreate.as_view(), name="character_create"),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(), name="character_detail")
]