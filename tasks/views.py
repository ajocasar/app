# tasks/views.py

from django.shortcuts import render
from .hangman import play_hangman

def play_hangman(request):
    if request.method == 'POST':
        game = play_hangman
        context = {'game': game}
        return render(request, 'inicio.html', context)
    else:
        return render(request, 'index.html')