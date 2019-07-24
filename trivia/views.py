from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import requests
import random

response = requests.get('https://opentdb.com/api.php?amount=1&type=multiple')
data = response.json()

correct_list = []

def gamepage(request):
    print("Viewed Gamepage")
    for item in data['results']:            # get to the right list
        question = item['question']
        correct = item['correct_answer']    # reference keys for correct answers
        choices = item['incorrect_answers'] # reverence keys for incorrect answers
        
        answers = []        
        for choice in choices:
            answers.append(choice)      # this adds the wrong answers to the list "answers"
        answers.append(correct)         # this adds the right answer to he list "answers"
        random.shuffle(answers)         # this randomizes all the answers from the list "answers"
        # correct_list.append(request.POST)
        
        context = {
        'trivia': question,
        'answer0': answers[0],
        'answer1': answers[1],
        'answer2': answers[2],
        'answer3': answers[3],
        'correct': correct,
    }

################### PROBLEM LIST ###################
# I need a way to refresh each page so new questions come up

        print(answers)
        print(correct)
        if 'a0' in request.POST:
            print("checked a0")
            answerzero = request.POST['a0']
            print("---", answerzero, "---")
            if answerzero == correct:
                print("---Correct!---")
                return redirect('correct/')
            else:
                print("---Sorry, wrong answer---")
                return redirect('incorrect/')
        
        if 'a1' in request.POST:
            print("checked a1")
            answerone = request.POST['a1']
            print("---", answerone, "---")
            if answerone == correct:
                print("---Correct!---")
                return redirect('correct/')
            else:
                print("---Sorry, wrong answer---")
                return redirect('incorrect/')

        if 'a2' in request.POST:
            print("checked a2")
            answertwo = request.POST['a2']
            print("---", answertwo, "---")
            if answertwo == correct:
                print("---Correct!---")
                return redirect('correct/')
            else:
                print("---Sorry, wrong answer---")
                return redirect('incorrect/')

        if 'a3' in request.POST:
            print("checked a3")
            answerthree = request.POST['a3']
            print("---", answerthree, "---")
            if answerthree == correct:
                print("---Correct!---")
                return redirect('correct/')
            else:
                print("---Sorry, wrong answer---")
                return redirect('incorrect/')

    return render(request, 'game.html', context)

def scores():
    correct_number = 0
    correct_number = len(correct_list)
    score = (correct_number * 100) / 3
    print("You scored", score, "%")

def correct(request):
    context = {}
    return render(request, 'correct.html', context)

def incorrect(request):
    context = {}
    return render(request, 'incorrect.html', context)

# gamepage()

# scores()

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

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    

