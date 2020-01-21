from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
import requests
import random
from trivia.models import QuestionAnswered 

# This code fixes the 'double' escape problem
# that produces garbage text during ' and "
from html.parser import HTMLParser

correct_list = []

def gamepage(request):
    if request.method == 'GET':
        response = requests.get('https://opentdb.com/api.php?amount=1&type=multiple')
        data = response.json()

        for item in data['results']:            # get to the right list
            question = item['question']
            request.session['correct_answer'] = item['correct_answer']
            request.session['incorrect_answers'] = item['incorrect_answers']
                # request.session allows data from two different dictionaries to persist through the requests
                # and allow them to be combined into one list

            h = HTMLParser()
            question = h.unescape(question)

            print(question)

            correct = request.session['correct_answer']    # reference keys for correct answers
            choices = request.session['incorrect_answers'] # reverence keys for incorrect answers
            
            answers = []        
            for choice in choices:
                answers.append(choice)      # this adds the wrong answers to the list "answers"
            answers.append(correct)         # this adds the right answer to he list "answers"
            random.shuffle(answers)         # this randomizes all the answers from the list "answers"

            h = HTMLParser()
            answers = h.unescape(answers)

            print(answers)
            print(correct)

            context = {   
            'trivia': question,
            'answer0': answers[0],
            'answer1': answers[1],
            'answer2': answers[2],
            'answer3': answers[3],
            'correct': correct,
        }

    else:
        correct = request.session['correct_answer']    # reference keys for correct answers
        choices = request.session['incorrect_answers'] # reverence keys for incorrect answers
        
        answers = []        
        for choice in choices:
            answers.append(choice)      # this adds the wrong answers to the list "answers"
        answers.append(correct)         # this adds the right answer to he list "answers"
        random.shuffle(answers)         # this randomizes all the answers from the list "answers"

        h = HTMLParser()
        answers = h.unescape(answers)

        context = {   
        'answer0': answers[0],
        'answer1': answers[1],
        'answer2': answers[2],
        'answer3': answers[3],
        'correct': correct,
        'number_already_answered': QuestionAnswered.objects.filter().count(),
    }

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
                print("---Picked 0, wrong answer---")
                return redirect('incorrect/')
        
        if 'a1' in request.POST:
            print("checked a1")
            answerone = request.POST['a1']
            print("---", answerone, "---")
            if answerone == correct:
                print("---Correct!---")
                return redirect('correct/')
            else:
                print("---Picked 1, wrong answer---")
                return redirect('incorrect/')

        if 'a2' in request.POST:
            print("checked a2")
            answertwo = request.POST['a2']
            print("---", answertwo, "---")
            if answertwo == correct:
                print("---Correct!---")
                return redirect('correct/')
            else:
                print("---Picked 2, wrong answer---")
                return redirect('incorrect/')

        if 'a3' in request.POST:
            print("checked a3")
            answerthree = request.POST['a3']
            print("---", answerthree, "---")
            if answerthree == correct:
                print("---Correct!---")
                return redirect('correct/')
            else:
                print("---Picked 3, wrong answer---")
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
    
    correct = request.session['correct_answer']    # reference keys for correct answers

    context = {
    'correct': correct,
    }
    return render(request, 'incorrect.html', context)

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
#            changed redirect from home to trivia game
            return redirect('trivia')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    
def create_user(data):
    user =  User.objects.create_user(username=data['username'],
        email=data['email'],
        password=data['password'],
        first_name=data['first_name'],
        last_name=data['last_name']
        )
    user.is_admin=False
    user.is_staff=False
    user.save()

#            Record user answers

def fraction(request):
    QuestionAnswered.objects.create(
        user=request.user,
        was_right=True,
    )
    QuestionAnswered.objects.count()
 
#            Getting "correct count"

    number_they_got_right = QuestionAnswered.objects.filter(
        user=request.user,
        was_right=True,
    ).count()
    
    return render(request, 'game.html', context)

################### TODO ###################
# - Styling of Correct and Incorrect pages
# - Improve responsiveness
# - Fix SignUp and LogIn pages
