from django.db import models

# Create your models here.
class Character(models.Model):

    name = models.CharField(max_length=100)
    real_name = models.CharField(max_length=100)
    img = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_hero = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Power(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="powers")

    def __str__(self):
        return self.title

class Team(models.Model):

    title = models.CharField(max_length=100)
    img = models.CharField(max_length=250, default=None)
    bio = models.TextField(max_length=500, default=None)
    characters = models.ManyToManyField(Character)

    def __str__(self):
        return self.title