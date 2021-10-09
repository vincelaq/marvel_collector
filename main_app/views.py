from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Character, Power, Team

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class CharacterDetail(View):

    def get(self, request, pk):
            character = Character.objects.get(id=pk)
            teams = Team.objects.all()
            charTeams = character.team_set.all() 
            return render(request, 'character_detail.html', {
                'teams': teams,
                'character': character,
                'charTeams': charTeams,
            })

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
            context["header"] = "Marvel Characters"
        return context

class CharacterCreate(CreateView):
    model = Character
    fields = ['name', 'real_name', 'img', 'bio', 'verified_hero']
    template_name = "character_create.html"

    def get_success_url(self):
        return reverse('character_detail', kwargs={'pk': self.object.pk})

class CharacterDelete(DeleteView):
    model = Character
    template_name = "character_delete_confirm.html"
    success_url = "/characters/"

class PowerCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        description = request.POST.get("description")
        character = Character.objects.get(pk=pk)
        Power.objects.create(title=title, description=description, character=character)
        return redirect('character_detail', pk=pk)

class TeamDetail(DetailView):
    model = Team
    template_name = "team_detail.html"

class TeamUpdate(UpdateView):
    model = Team
    fields = ['title', 'img', 'bio', 'characters']
    template_name = "team_update.html"

    def get_success_url(self):
        return reverse('team_detail', kwargs={'pk': self.object.pk})

class TeamList(TemplateView):
    template_name = "team_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")

        if title != None:
            context["teams"] = Team.objects.filter(title__icontains=title)
            context["header"] = f"Searching for {title}"
        else:
            context["teams"] = Team.objects.all()
            context["header"] = "Marvel Team Affiliations"
        return context

class TeamCreate(CreateView):
    model = Team
    fields = ['title', 'img', 'bio', 'characters']
    template_name = "team_create.html"

    def get_success_url(self):
        return reverse('team_detail', kwargs={'pk': self.object.pk})

class TeamDelete(DeleteView):
    model = Team
    template_name = "team_delete_confirm.html"
    success_url = "/teams/"

class TeamCharacterAssoc(View):
    
    def get(self, request, pk, character_pk):
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            Team.objects.get(pk=pk).characters.remove(character_pk)
        if assoc == "add":
            Team.objects.get(pk=pk).characters.add(character_pk)
        return redirect(f'/teams/{pk}/')