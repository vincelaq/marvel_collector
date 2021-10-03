from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Character

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class CharacterDetail(DetailView):
    model = Character
    template_name = "character_detail.html"

class CharacterList(TemplateView):
    template_name = "character_list.html"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")

        if name != None:
            context["characters"] = Character.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["characters"] = Character.objects.all()
            context["header"] = "Trending Characters"
        return context

class CharacterCreate(CreateView):
    model = Character
    fields = ['name', 'real_name', 'img', 'bio', 'verified_hero']
    template_name = "character_create.html"
    success_url = "/characters/"