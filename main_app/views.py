from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Character

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class CharacterDetail(DetailView):
    model = Character
    template_name = "character_detail.html"

class CharacterUpdate(UpdateView):
    model = Character
    fields = ['name', 'real_name', 'img', 'bio', 'verified_hero']
    template_name = "character_update.html"

    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})

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

    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})

class CharacterDelete(DeleteView):
    model = Character
    template_name = "character_delete_confirmation.html"
    success_url = "/characters/"