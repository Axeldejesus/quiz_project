from django.shortcuts import render
# render sert à afficher un template
from ..models import Question, Utilisateur
import random

def initialiser_session(request, theme_id):
    # cette fonction permet de récupérer les questions de la base de données
    # en paramètre request permet de récupérer les données de la requête
    # theme_id permet de récupérer l'id du thème choisi
    questions_query = Question.objects.filter(theme_id=theme_id) if theme_id else Question.objects.all()
    # questions_query est un objet de type QuerySet cet à dire une liste de questions
    # Question.objects.filter permet de récupérer les questions du thème choisi
    # theme_id est l'id du thème choisi
    # if theme_id else Question.objects.all() permet de récupérer toutes les questions si aucun thème n'est choisi
    questions_order = random.sample(list(questions_query), min(len(questions_query), 30))
    # questions_order est une liste de questions aléatoires
    # random.sample permet de récupérer des questions aléatoires
    # list(questions_query) permet de convertir questions_query en liste
    # min(len(questions_query), 10) permet de récupérer 10 questions si questions_query contient plus de 20 questions
    request.session['questions_order'] = [q.id for q in questions_order]
    # request.session permet de créer une session
    # une session c'est un espace de stockage qui permet de stocker des données
    # [quesion_order] permet de récupérer les id des questions
    # q.id permet de récupérer l'id de la question, q correspond à une question
    request.session['question_index'] = 0
    # request.session['question_index'] permet de récupérer l'index de la question
    # ici on initialise l'index à 0
    request.session['time_left'] = 120
    # request.session['time_left'] permet de récupérer le temps restant
    # ici on initialise le temps restant à 50 secondes
    

def traiter_reponse(request, current_question, utilisateur, question_index):
    # cette fonction permet de traiter la réponse de l'utilisateur
    # elle prend en paramètre request, current_question, utilisateur et question_index
    # request permet de récupérer les données de la requête
    # current_question permet de récupérer la question courante
    # utilisateur permet de récupérer l'utilisateur
    # question_index permet de récupérer l'index de la question
    user_answer = request.POST.get('reponse', '').strip().lower()
    # user_answer permet de récupérer la réponse de l'utilisateur
    # request.POST permet de récupérer les données envoyées par l'utilisateur
    # get('reponse', '') permet de récupérer la réponse de l'utilisateur
    # strip() permet de supprimer les espaces avant et après la réponse de l'utilisateur
    # lower() permet de convertir la réponse de l'utilisateur en minuscule
    time_taken_str = request.POST.get('timeTaken', '120')
    # time_taken_str permet de récupérer le temps pris par l'utilisateur pour répondre à la question
    # request.POST permet de récupérer les données envoyées par l'utilisateur
    # get('timeTaken', '120') permet de récupérer le temps pris par l'utilisateur pour répondre à la question
    try:
        # try permet de tester si le temps pris par l'utilisateur pour répondre à la question est un nombre
        time_taken = float(time_taken_str) if time_taken_str else 0
        # time_taken permet de récupérer le temps pris par l'utilisateur pour répondre à la question
        # float(time_taken_str) permet de convertir le temps pris par l'utilisateur pour répondre à la question en nombre
        # if time_taken_str else 0 permet de récupérer 0 si le temps pris par l'utilisateur pour répondre à la question est vide
    except ValueError:
        # except permet de récupérer une erreur si le temps pris par l'utilisateur pour répondre à la question n'est pas un nombre
        time_taken = 0
        # ici on initialise le temps pris par l'utilisateur pour répondre à la question à 0

    if user_answer == current_question.Reponse_correcte.lower():
        # if permet de tester si la réponse de l'utilisateur est correcte
        # == permet de tester si la réponse de l'utilisateur est égale à la réponse correcte
        # current_question.Reponse_correcte.lower() permet de convertir la réponse correcte en minuscule
        points = calculer_points(time_taken)
        # points permet de calculer les points de l'utilisateur
        utilisateur.Score += points
        # utilisateur.score permet de récupérer le score de l'utilisateur
        # += permet d'ajouter les points de l'utilisateur à son score
        utilisateur.save() 
        
        # utilisateur.save() permet de sauvegarder le score de l'utilisateur
        return None, question_index + 1
        # return None, question_index + 1 permet de retourner None et l'index de la question suivante
    else:
        return "Réponse incorrecte, veuillez réessayer.", question_index
        # return, question_index permet de retourner un message d'erreur et l'index de la question courante

def questions_view(request):
    # cette fonction permet d'afficher les questions
    theme_id = request.GET.get('theme_id')
    # theme_id permet de récupérer l'id du thème choisi
    utilisateur = Utilisateur.objects.last()
    # utilisateur permet de récupérer le dernier utilisateur
    if request.method == 'GET' or 'questions_order' not in request.session:
        # if permet de tester si la méthode de la requête est GET ou si questions_order n'est pas dans la session
        initialiser_session(request, theme_id)
        # initialiser_session permet d'initialiser la session
        # request permet de récupérer les données de la requête
        # theme_id permet de récupérer l'id du thème choisi
    questions_order = request.session.get('questions_order')
    question_index = request.session.get('question_index', 0)
    time_left = request.session.get('time_left', 120)

    
    if time_left <= 0:
        # if permet de tester si le temps restant est inférieur ou égal à 0
        return terminer_quiz(request, utilisateur)
        # terminer_quiz permet de terminer le quiz

    current_question = Question.objects.get(id=questions_order[question_index])
    # current_question permet de récupérer la question courante
    # Question.objects.get permet de récupérer la question courante
    # id=questions_order[question_index] permet de récupérer l'id de la question courante
    error_message = None
    # error_message permet de récupérer un message d'erreur

    if request.method == 'POST':
        # if permet de tester si la méthode de la requête est POST
        # c'est à dire si l'utilisateur a cliqué sur le bouton valider
        time_left = int(request.POST.get('timeLeft', 120))
        # time_left permet de récupérer le temps restant
        # request.POST permet de récupérer les données envoyées par l'utilisateur
        # get('timeLeft', 50) permet de récupérer le temps restant
        request.session['time_left'] = time_left
        # request.session['time_left'] permet de récupérer le temps restant

        error_message, question_index = traiter_reponse(request, current_question, utilisateur, question_index)

        request.session['question_index'] = question_index  
        # request.session['question_index'] permet de récupérer l'index de la question

    
    if time_left <= 0:
        # if permet de tester si le temps restant est inférieur ou égal à 0
        return terminer_quiz(request, utilisateur)
        # terminer_quiz permet de terminer le quiz

    next_question = obtenir_prochaine_question(question_index, questions_order)
    # next_question permet de récupérer la question suivante

    return render(request, 'index.html', {
        # render permet d'afficher un template
        # request permet de récupérer les données de la requête
        # 'index.html' permet de récupérer le template index.html
        'question': next_question,
        # 'question' permet de récupérer la question suivante
        'pseudo': utilisateur.Nom_Utilisateur if utilisateur else "Utilisateur inconnu",
        # 'pseudo' permet de récupérer le pseudo de l'utilisateur
        'error_message': error_message,
        # 'error_message' permet de récupérer un message d'erreur
        'theme_id': theme_id,
        # 'theme_id' permet de récupérer l'id du thème choisi
        'time_left': time_left,
        # 'time_left' permet de récupérer le temps restant
        'Score': utilisateur.Score if utilisateur else 0
        # 'score' permet de récupérer le score de l'utilisateur
    })

def obtenir_prochaine_question(question_index, questions_order):
    # cette fonction permet de récupérer la question suivante
    # elle prend en paramètre question_index et questions_order
    # question_index permet de récupérer l'index de la question
    # questions_order permet de récupérer la liste des questions
    if question_index < len(questions_order):
        # if permet de tester si l'index de la question est inférieur à la longueur de la liste des questions
        # len(questions_order) permet de récupérer la longueur de la liste des questions
        return Question.objects.get(id=questions_order[question_index])
        # Question.objects.get permet de récupérer la question suivante
        # id=questions_order[question_index] permet de récupérer l'id de la question suivante
    else:
        return None
        # return None permet de retourner None

def terminer_quiz(request, utilisateur):
    # cette fonction permet de terminer le quiz
    # elle prend en paramètre request et utilisateur
    # request permet de récupérer les données de la requête
    # utilisateur permet de récupérer l'utilisateur
    utilisateur.refresh_from_db()
    # utilisateur.refresh_from_db() permet de rafraîchir les données de l'utilisateur
    del request.session['questions_order']
    del request.session['question_index']
    del request.session['time_left']
    return render(request, 'score.html', {'Score': utilisateur.Score})
    # render permet d'afficher un template
    # request permet de récupérer les données de la requête
    # 'score.html' permet de récupérer le template score.html
    # 'score' permet de récupérer le score de l'utilisateur

def calculer_points(time_taken):
    # cette fonction permet de calculer les points de l'utilisateur
    # elle prend en paramètre time_taken
    if time_taken < 10:
        # if permet de tester si le temps pris par l'utilisateur pour répondre à la question est inférieur à 10 secondes
        return 3
        # return 3 permet de retourner 3 points
    elif time_taken < 20:
        # elif permet de tester si le temps pris par l'utilisateur pour répondre à la question est inférieur à 20 secondes
        return 2
        # return 2 permet de retourner 2 points
    else:
        # else permet de récupérer le temps pris par l'utilisateur pour répondre à la question
        return 1
        # return 1 permet de retourner 1 point




