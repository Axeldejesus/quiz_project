from django.db import models

class Question(models.Model):
    # cette classe permet de créer recupérer les questions de la base de données
    # models.Model permet de dire que cette classe est un modèle
    id = models.AutoField(primary_key=True, db_column='id_Questions')
    # id_Questions est la clé primaire de la table questions
    # models.AutoField permet de recuperer un champ de type entier
    # primary_key=True permet de dire que ce champ est la clé primaire
    # db_column='id_Questions' permet de dire que le nom de la colonne dans la base de données est id_Questions
    # si on ne met pas db_column, le nom de la colonne dans la base de données sera id
    # c'est important de spécifier db_column car le nom de la colonne dans la base de données est id_Questions
    Texte_Questions = models.CharField(max_length=255)
    # Texte_Questions est un champ de type texte
    # models.CharField permet de recuperer un champ de type texte
    # max_length=255 permet de dire que la longueur maximale du champ est de 255 caractères
    Reponse_correcte = models.CharField(max_length=255)
    # Reponse_correcte est un champ de type texte
    # models.CharField permet de recuperer un champ de type texte
    # max_length=255 permet de dire que la longueur maximale du champ est de 255 caractères
    theme = models.ForeignKey('Theme', on_delete=models.CASCADE, db_column='id_Theme')
    # theme est un champ de type clé étrangère
    # models.ForeignKey permet de recuperer un champ de type clé étrangère
    # 'Theme' permet de dire que la clé étrangère est liée à la table Theme
    # on_delete=models.CASCADE permet de dire que si on supprime un thème, toutes les questions liées à ce thème seront supprimées
    # db_column='id_Theme' permet de dire que le nom de la colonne dans la base de données est id_Theme
    # si on ne met pas db_column, le nom de la colonne dans la base de données sera theme_id
    # c'est important de spécifier db_column car le nom de la colonne dans la base de données est id_Theme
    

    class Meta:
        # cette classe permet de dire que le nom de la table dans la base de données est questions
        # si on ne met pas cette classe, le nom de la table dans la base de données sera quiz_question
        db_table = 'questions'
        # db_table permet de dire que le nom de la table dans la base de données est questions
        app_label = 'quiz'
        # app_label permet de dire que le nom de l'application est quiz

class Theme(models.Model):
    # cette classe permet de créer recupérer les thèmes de la base de données
    # elle prend les mêmes arguments que la classe Question
    # models.Model permet de dire que cette classe est un modèle
    id_Theme = models.AutoField(primary_key=True)
    # id_Theme est la clé primaire de la table theme
    # models.AutoField permet de recuperer un champ de type entier
    # primary_key=True permet de dire que ce champ est la clé primaire
    Nom_theme = models.CharField(max_length=255)
    # Nom_theme est un champ de type texte
    # models.CharField permet de recuperer un champ de type texte
    # max_length=255 permet de dire que la longueur maximale du champ est de 255 caractères
    def __str__(self):
        return self.Nom_theme
    class Meta:
        # cette classe permet de dire que le nom de la table dans la base de données est theme
        db_table = 'theme'
        # db_table permet de dire que le nom de la table dans la base de données est theme

class Utilisateur(models.Model):
    # cette classe permet de créer recupérer les utilisateurs de la base de données
    id = models.AutoField(primary_key=True, db_column='id_Utilisateur')
    # id_Utilisateur est la clé primaire de la table utilisateur
    # models.AutoField permet de recuperer un champ de type entier
    # primary_key=True permet de dire que ce champ est la clé primaire
    # db_column='id_Utilisateur' permet de dire que le nom de la colonne dans la base de données est id_Utilisateur
    Nom_Utilisateur = models.CharField(max_length=255)
    # Nom_Utilisateur est un champ de type texte
    # models.CharField permet de recuperer un champ de type texte
    # max_length=255 permet de dire que la longueur maximale du champ est de 255 caractères
    Score = models.IntegerField(default=0)
    # score est un champ de type entier
    # models.IntegerField permet de recuperer un champ de type entier
    # default=0 permet de dire que la valeur par défaut du champ est 0
    Temps = models.IntegerField(default=120)
    # Temps est un champ de type entier
    # models.IntegerField permet de recuperer un champ de type entier
    # default=50 permet de dire que la valeur par défaut du champ est 50
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    Role = models.CharField(max_length=50, default='user')
    


    class Meta:
        # cette classe permet de dire que le nom de la table dans la base de données est utilisateur
        db_table = 'utilisateur'
        # db_table permet de dire que le nom de la table dans la base de données est utilisateur

class ImageQuiz(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    nom = models.CharField(max_length=100)
    chemin_image = models.CharField(max_length=255)
    reponse_correcte = models.CharField(max_length=100)

    
    class Meta :
        db_table = 'image_quiz'