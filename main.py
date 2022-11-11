import os
from typing import NamedTuple

questions = []
answers = []
correct_answers = []
points = []

class answer_struct(NamedTuple):
    a: str = ""
    b: str = ""
    c: str = ""
    d: str = ""
    e: str = ""
    f: str = ""

num_questions = 0
while(num_questions < 5 or num_questions > 25):
    num_questions = int(input("How many questions do you wish to create?(25 max, 5 min) "))
    
    if(num_questions < 5 or num_questions > 25):
        print("The number of questions must be bigger than 5 and smaller than 25!")

num_answers = 0
while(num_answers < 2 or num_answers > 6):
    num_answers = int(input("How many answers per question do you want?(6 max, 2 min) "))

    if(num_answers < 2 or num_answers > 6):
        print("The number of answers must be bigger than 2 and smaller than 6!")


max_points = 0
while(max_points < num_questions):
    max_points = int(input("What is the max ammount of points in your quizz? "))
    if(max_points < num_questions):
        print("The max points has to be at least equal to the number of questions.")

print("Define your questions below: ")
for i in range(num_questions):
    a, b, c, d, e, f = "", "", "", "", "", ""

    points.append(max_points / num_questions)

    questions.append(str(input("> ")))
    
    match num_answers:
        case 2:
            a = str(input("a > "))        
            b = str(input("b > "))
        case 3:
            a = str(input("a > "))        
            b = str(input("b > "))        
            c = str(input("c > "))
        case 4:
            a = str(input("a > "))        
            b = str(input("b > "))        
            c = str(input("c > "))
            d = str(input("d > "))
        case 5:
            a = str(input("a > "))        
            b = str(input("b > "))        
            c = str(input("c > "))
            d = str(input("d > "))
            e = str(input("e > "))
        case 6:
            a = str(input("a > "))        
            b = str(input("b > "))        
            c = str(input("c > "))
            d = str(input("d > "))
            e = str(input("e > "))
            f = str(input("f > "))

    answers.append(answer_struct(a, b, c, d, e, f))

    correct = str(input("What is the correct answer for this question?(a, b, c, d, e or f) "))

    match correct:
        case 'a':
            correct_answers.append(answers[i].a)
        case 'b':
            correct_answers.append(answers[i].b)
        case 'c':
            correct_answers.append(answers[i].c)
        case 'd':
            correct_answers.append(answers[i].d)
        case 'e':
            correct_answers.append(answers[i].e)
        case 'f':
            correct_answers.append(answers[i].f)


if not os.path.exists("files"):
    os.makedirs("files")

file_name = str(input("Name of the file to be saved: files/"))
file_name = f"files/{file_name}"

file = open(file_name, "a")

for i in range(num_questions):
    file.write(f"{questions[i]},{answers[i]},{correct_answers[i]},{points[i]}\n")

file.close()

print(f"Quizz has been saved to {os.path.abspath(file_name)}.")
