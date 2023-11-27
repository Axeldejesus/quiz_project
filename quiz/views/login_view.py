from django.shortcuts import render, redirect
from ..models import Utilisateur
from ..forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            pseudo = form.cleaned_data['pseudo']

            # Définir le rôle en fonction du pseudo
            role = 'admin' if pseudo == 'Ashene' else 'user'

            # Vérifier si l'utilisateur existe déjà
            utilisateur, created = Utilisateur.objects.get_or_create(
                Nom_Utilisateur=pseudo,
                defaults={'Score': 0, 'Temps': 120, 'Role': role}
            )

            if not created:
                # Si l'utilisateur existe déjà, mettez à jour ses informations si nécessaire
                utilisateur.Temps = 120  # Réinitialiser le temps, par exemple
                utilisateur.save()

            return redirect('home')  # Assurez-vous que 'home' est bien l'URL de redirection souhaitée
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
