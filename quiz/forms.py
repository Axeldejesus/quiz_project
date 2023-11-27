from django import forms
# from django import forms sert à importer les formulaires de Django

class LoginForm(forms.Form):
    # class LoginForm est un formulaire de Django
    # forms.Form est une classe de Django qui permet de créer des formulaires
    pseudo = forms.CharField(label="Entrez votre pseudo")
    # pseudo est un champ de formulaire qui contient du texte
    # forms.CharField est un champ de formulaire qui contient du texte
    # label="Entrez votre pseudo" est le texte qui s'affiche dans le formulaire
