# En hangman/views.py

from django.shortcuts import render
import random

def choose_word():
    words = ['python', 'java', 'javascript', 'ruby', 'php', 'html', 'css']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def play_hangman(request):
    word = choose_word()
    guessed_letters = []

    if request.method == 'POST':
        guess = request.POST.get('guess', '').lower()
        guessed_letters.append(guess)

    displayed = display_word(word, guessed_letters)
    context = {
        'word': displayed,
        'guessed_letters': guessed_letters,
        'attempts_left': 6 - len([x for x in guessed_letters if x not in word]),
    }

    return render(request, 'hangman/game.html', context)