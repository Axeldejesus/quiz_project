from django.contrib import admin
# django.contrib : contient les applications par défaut de Django
# admin : application de gestion de l'administration de Django
from .models import Question, Theme, Utilisateur, ImageQuiz

class QuestionAdmin(admin.ModelAdmin):
    # la classe QuestionAdmin hérite de la classe ModelAdmin
    # ModelAdmin permet de personnaliser l'interface d'administration
    list_display = ('Texte_Questions', 'Reponse_correcte', 'display_theme')
    # list_display permet de dire quels champs afficher dans la liste des questions
    search_fields = ('Texte_Questions', 'Reponse_correcte')
    # search_fields permet de dire quels champs utiliser pour la recherche

    def display_theme(self, obj):
        # cette fonction permet de récupérer le thème de la question
        return obj.theme.Nom_theme
        # obj.theme permet de récupérer le thème de la question
    display_theme.short_description = 'Theme'
    # display_theme.short_description permet de dire que le nom de la colonne dans l'interface d'administration est Theme


class ThemeAdmin(admin.ModelAdmin):
    list_display = ('Nom_theme',)
    search_fields = ('Nom_theme',)

class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('Nom_Utilisateur', 'Score', 'Temps', 'Role')
    search_fields = ('Nom_Utilisateur',)
    list_filter = ('Role',)

class ImageQuizAdmin(admin.ModelAdmin):
    list_display = ('nom', 'chemin_image', 'reponse_correcte')
    search_fields = ('nom', 'reponse_correcte')

admin.site.register(Question, QuestionAdmin)
# admin.site.register permet de dire que la classe Question est gérée par l'interface d'administration
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Utilisateur, UtilisateurAdmin)
admin.site.register(ImageQuiz, ImageQuizAdmin)


