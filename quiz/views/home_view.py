from django.shortcuts import render
from ..models import Utilisateur

def home_view(request):
    utilisateur = Utilisateur.objects.last()
    utilisateur.score = 0
    utilisateur.save()
    return render(request, 'home.html')
