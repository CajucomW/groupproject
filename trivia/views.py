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
<<<<<<< HEAD
        random.shuffle(answers)         # this randomizes all the answers from the list "answers"

        print(answers)

        user_answer = input("Type your answer here: ")
        if user_answer in correct:
            correct_list.append(user_answer)
            print("You got it!")
        else:
            print("Sorry. The answer is", correct + ".")

        # print(correct_list)
    context = {
        'trivia': question,
        'answer0': answers[0],
        'answer1': answers[1],
        'answer2': answers[2],
        'answer3': answers[3],
    }
=======
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
        

>>>>>>> f65ffb460c4fbdb4cdbaf87421635c35ae1dac35
    return render(request, 'game.html', context)

def scores():
    correct_number = 0
    correct_number = len(correct_list)
    score = (correct_number * 100) / 3
    print("You scored", score, "%")

# gamepage()

# scores()
<<<<<<< HEAD



# def gamepage(request):
#     context = {
#         trivia =
#     }
#     return render(request, 'game.html', context)

#log in and log out

def login_user(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect("index")
        else:
            messages.success(request, 'Error logging in')
            return redirect('login')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    print('logout function working')
    return redirect('login')
=======
>>>>>>> f65ffb460c4fbdb4cdbaf87421635c35ae1dac35
