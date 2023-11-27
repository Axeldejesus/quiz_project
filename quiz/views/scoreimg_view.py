from django.shortcuts import render
from ..models import Utilisateur

def scoreimg_view(request):
    # Cette fonction permet d'afficher la page du score
    try:
        # try permet de gérer les erreurs
        utilisateur = Utilisateur.objects.last()  
        # On récupère le dernier utilisateur créé
        score = utilisateur.score if utilisateur else 0
        # score contient le score de l'utilisateur
    except Exception as e:
        # Si une erreur se produit, on affiche le message d'erreur
        score = 0
        # score vaut 0
        
    return render(request, 'scoreimg.html', {'score': score})
    # On affiche la page du score
    # avec le score de l'utilisateur