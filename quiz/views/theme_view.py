from django.shortcuts import render
from ..models import Theme, Utilisateur

def theme_view(request):
   # Cette fonction permet d'afficher la page des thèmes
    utilisateur = Utilisateur.objects.last()
    # On récupère le dernier utilisateur créé
    if utilisateur:
        # Si un utilisateur existe, on récupère son pseudo
        utilisateur.Score = 0
        # On remet son score à 0
        utilisateur.save()
        # On sauvegarde l'utilisateur
        pseudo = utilisateur.Nom_Utilisateur
        # pseudo contient le pseudo de l'utilisateur
    else:
        pseudo = "Invité"
        # Si aucun utilisateur n'existe, pseudo vaut "Invité"

    themes = Theme.objects.all() 
    # On récupère tous les thèmes
    return render(request, 'theme.html', {'themes': themes, 'pseudo': pseudo})
    # On affiche la page des thèmes
    # avec la liste des thèmes et le pseudo de l'utilisateur

