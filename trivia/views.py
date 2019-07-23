from django.shortcuts import render
from django import forms
import requests
import random

response = requests.get('https://opentdb.com/api.php?amount=1&type=multiple')
data = response.json()
user_answer = None

correct_list = []
# def welcome():

#     print("Welcome to Our Group Project!")
#     username = input("Please enter a Username: ")
    
# welcome()

def gamepage(request):

    print("---Viewed Gamepage---")
    for item in data['results']:            # get to the right list
        question = item['question']

    for item in data['results']:            # get to the right list
        correct = item['correct_answer']    # reference keys for correct answers
        choices = item['incorrect_answers'] # reverence keys for incorrect answers
        answers = []
        for choice in choices:
            answers.append(choice)      # this adds the wrong answers to the list "answers"
        answers.append(correct)         # this adds the right answer to he list "answers"
        random.shuffle(answers)         # this randomizes all the answers from the list "answers"    if answers[0] in correct:
        correct_list.append(user_answer)
        
        context = {
            'trivia': question,
            'answer0': answers[0],
            'answer1': answers[1],
            'answer2': answers[2],
            'answer3': answers[3],
        }

    if request.method == 'POST':
        

    return render(request, 'game.html', context)

def scores():
    correct_number = 0
    correct_number = len(correct_list)
    score = (correct_number * 100) / 3
    print("You scored", score, "%")

# gamepage()

# scores()
