import sys
import random
from questions import QUESTIONS
def isAnswerCorrect(question, answer):
    if answer == question["answer"]:
        return True
    else:
        return False

def lifeline(ques):
    l=[]
    a=[]
    a.append(ques["option1"])
    a.append(ques["option2"])
    a.append(ques["option3"])
    a.append(ques["option4"])
    a.remove(ques["option"+str(ques["answer"])])
    q=random.choice(a)
    l.append(ques["option"+str(ques["answer"])])
    l.append(q)
    print(f'\t\tOptions:')

    reducedOptionList = []
    for x in range(len(l)):
        for idx,op in enumerate(ques):
            if ques[f'option{idx+1}'] == l[x]:
                reducedOptionList.append(f'\t\t\tOptions {idx+1}: {l[x]}')
                break

    for op in sorted(reducedOptionList):
        print(op)
    ans1 = input('Your choice ( 1-4) : ')
    return ans1




def kbc():
    i=0
    money=0
    for i in range (0,15):
        print(f'\tQuestion {i+1}: {QUESTIONS[i]["name"]}')
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
        print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
        print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
        print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
        ans = input('Your choice ( 1-4 ) : ')
        if ans=="lifeline":
            ans=lifeline(QUESTIONS[i])

        if(i+1<=5):
            minamt=0
            if isAnswerCorrect(QUESTIONS[i], int(ans)):
                print("correct")
                print("you won Rs", QUESTIONS[i]["money"])
                money = money + QUESTIONS[i]["money"]


            else:
                print("Incorrect")
                print("the correct answer is", QUESTIONS[i]["answer"])
                print("The total amount won is Rs", minamt)
                sys.exit()

        if (i + 1 >5 and i+1<=11):
            minamt=10000
            if isAnswerCorrect(QUESTIONS[i], int(ans)):
                print("correct")
                print("you won Rs", QUESTIONS[i]["money"])
                money = minamt + QUESTIONS[i]["money"]


            else:
                print("Incorrect")
                print("the correct answer is", QUESTIONS[i]["answer"])
                print("The total amount won is Rs", minamt)
                sys.exit()

        if (i + 1 > 11):
            minamt=320000
            if isAnswerCorrect(QUESTIONS[i], int(ans)):
                print("correct")
                print("you won Rs", QUESTIONS[i]["money"])
                money = minamt + QUESTIONS[i]["money"]


            else:
                print("Incorrect")
                print("the correct answer is", QUESTIONS[i]["answer"])
                print("The total amount won is Rs", minamt)
                sys.exit()
kbc()