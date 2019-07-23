from django.shortcuts import render, redirect
from django import forms
import requests
import random

response = requests.get('https://opentdb.com/api.php?amount=1&type=multiple')
data = response.json()

correct_list = []
# def welcome():

#     print("Welcome to Our Group Project!")
#     username = input("Please enter a Username: ")
    
# welcome()

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
    }
        print(answers)
        print(correct)
        if 'a0' in request.POST:
            print("checked a0")
            answerzero = request.POST['a0']
            print("---", answerzero, "---")
            if answerzero == correct:
                print("---Correct!---")
        else:
            print("---Sorry, wrong answer---")
        if 'a1' in request.POST:
            print("checked a1")
            answerone = request.POST['a1']
            print("---", answerone, "---")
            if answerone == correct:
                print("---Correct!---")
        else:
            print("---Sorry, wrong answer---")
        if 'a2' in request.POST:
            print("checked a2")
            answertwo = request.POST['a2']
            print("---", answertwo, "---")
            if answertwo == correct:
                print("---Correct!---")
        else:
            print("---Sorry, wrong answer---")
        if 'a3' in request.POST:
            print("checked a3")
            answerthree = request.POST['a3']
            print("---", answerthree, "---")
            if answerthree == correct:
                print("---Correct!---")
        else:
            print("---Sorry, wrong answer---")

            # one = request.POST['answer1']
            # if one in correct:
            #     print("Correct1")
            # two = request.POST['answer2']
            # if two in correct:
            #     print("Correct2")
            # three = request.POST['answer3']
            # if three in correct:
            #     print("Correct3")


        # print(correct)
        # print(answers)
    
    # if request.method == 'POST':
    #     if answer0 in correct:
    #         print("---viewed 0---")
    #         print("correct")
    #         return redirect('/')
    #     elif answer1 in correct:
    #         print("---viewed 1---")
    #         print("correct")
    #         return redirect('/')  
    #     elif answers2 in correct:
    #         print("---viewed 2---")
    #         print("correct")
    #         return redirect('/')      
    #     elif answers3 in correct:
    #         print("---viewed 3---")
    #         print("correct")
    #         return redirect('/')
    #     else:
    #         print("Sorry. The answer is", correct + ".")
    
    return render(request, 'game.html', context)

def scores():
    correct_number = 0
    correct_number = len(correct_list)
    score = (correct_number * 100) / 3
    print("You scored", score, "%")

# gamepage()

# scores()
