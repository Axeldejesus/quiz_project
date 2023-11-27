from django.shortcuts import render, redirect
from django.utils import timezone
from ..models import ImageQuiz, Utilisateur
import random

def gameimg_view(request):
    utilisateur = Utilisateur.objects.last()  # Remplacer par l'utilisateur authentifié si possible

    # Initialisation ou récupération de la session de jeu
    if request.method == 'GET' or 'game_start_time' not in request.session:
        images_query = ImageQuiz.objects.all()
        images_order = random.sample(list(images_query), min(len(images_query), 50))
        request.session['images_order'] = [img.id for img in images_order]
        request.session['image_index'] = 0
        request.session['game_start_time'] = timezone.now().timestamp()  # Enregistrer le temps de début
        utilisateur.Score = 0  # Réinitialiser le score
        utilisateur.save()

    images_order = request.session.get('images_order')
    image_index = request.session.get('image_index', 0)

    # Calcul du temps restant
    start_time = request.session.get('game_start_time')
    time_elapsed = timezone.now().timestamp() - start_time
    time_left = max(120 - time_elapsed, 0)  # 120 secondes - temps écoulé

    if time_left <= 0 or image_index >= len(images_order):
        # Terminer le jeu si le temps est écoulé ou toutes les images ont été montrées
        return terminer_jeu(request, utilisateur)

    current_image = ImageQuiz.objects.get(id=images_order[image_index])
    error_message = None

    if request.method == 'POST':
        user_answer = request.POST.get('reponse', '').strip().lower()
        if user_answer == current_image.reponse_correcte.lower():
            utilisateur.Score += 1  # Augmenter le score pour chaque réponse correcte
            utilisateur.save()
            request.session['image_index'] += 1
        else:
            error_message = "Mauvaise réponse"

    image_index = request.session.get('image_index', 0)
    next_image = ImageQuiz.objects.get(id=images_order[image_index]) if image_index < len(images_order) else None

    return render(request, 'gameimg.html', {
        'image': next_image,
        'time_left': int(time_left),
        'Score': utilisateur.Score,
        'error_message': error_message
    })

def terminer_jeu(request, utilisateur):
    utilisateur.refresh_from_db()
    del request.session['images_order']
    del request.session['image_index']
    del request.session['game_start_time']
    return render(request, 'scoreimg.html', {'Score': utilisateur.Score}) 







