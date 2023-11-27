"""
URL configuration for quiz_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.shortcuts import redirect
from quiz.views.login_view import login_view
from quiz.views.theme_view import theme_view
from quiz.views.questions_view import questions_view
from quiz.views.score_view import score_view
from quiz.views.home_view import home_view
from quiz.views.gameimg_view import gameimg_view
from quiz.views.scoreimg_view import scoreimg_view
from quiz.views.serializers_view import QuestionViewSet, ThemeViewSet, ImageQuizViewSet
from rest_framework.routers import DefaultRouter
from django.contrib import admin


router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'themes', ThemeViewSet)
router.register(r'imagequiz', ImageQuizViewSet)


urlpatterns = [
    path('', lambda request: redirect('login/'), name='root'),  # Redirection de la racine vers la page de login
    path('home/', home_view, name='home'),  # Page d'accueil après la connexion
    path('gameimg/', gameimg_view, name='gameimg'),  # Page du jeu "Qui est-ce ?"
    path('login/', login_view, name='login'),  # Page de login
    path('questions/', questions_view, name='questions_view'),
    path('themes/', theme_view, name='themes'),
    path('questions/<int:id_Theme>/', questions_view, name='questions_by_theme'),
    path('score/', score_view, name='score'),
    path('scoreimg/', scoreimg_view, name='scoreimg'),
    path('quiz-app-api/', include(router.urls)),  # Chemin pour l'API REST
    path('admin/', admin.site.urls),
    # ... autres chemins
]











