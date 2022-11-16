import os
import sys
import base64
import time

from typing import NamedTuple
from dotenv import load_dotenv

load_dotenv()
KEY = str(os.getenv('KEY'))
TIMES = int(str(os.getenv('TIMES')))

class quizzer:
    credentials_file = "files/.credentials.txt"
    logged_user = str

    def __init__(self):
        account = str(input("Do you have an account already? (y or n) "))

        if account == "y" or account == "Y" or account == "yes":
            self.login()
            self.create_quizz()
        elif account == "n" or account == "N" or account == "no":
            self.create_account()
            self.create_quizz()

    def create_account(self):
        credentials = open(self.credentials_file, "a")

        username = str(input("Username: "))
        password = str(input("Password: "))

        for i in range(TIMES):
            password_bytes = password.encode(KEY)
            base64_bytes = base64.b64encode(password_bytes)
            password = base64_bytes.decode(KEY)

        credentials.write(f"{username} {password}\n")
        credentials.close()
        
        print("Your account has been created!")
        self.logged_user = username
        time.sleep(0.5)

    def login(self):
        credentials = open(self.credentials_file, "r")
        users = {}

        lines = credentials.readlines()
        for i in lines:
            line = i.split(" ")
            users[line[0]] = line[1][:-1]

        username = str(input("Username: "))

        if username in users:
            logged = False
            tries = 4

            while(not logged and tries > 0):
                password = str(input("Password: "))
                users_password = users[username]

                for i in range(TIMES):
                    base64_bytes = users_password.encode(KEY)
                    password_bytes = base64.b64decode(base64_bytes)
                    users_password = password_bytes.decode(KEY)

                if(users_password == password):
                    logged = True
                    print("You are logged in.")
                    self.logged_user = username
                    time.sleep(0.5)
                else:
                    tries -= 1
                    if(tries > 0):
                        print(f"Password is incorrect, you have {tries} left.")
                    else:
                        sys.exit("The password is incorrect and you are out of tries. Please try again later.")
        else:
            print("Your username does not exist. Try again.")
            account = str(input("Do you want to create a new account? (y or n) "))

            if account == "n" or account == "N" or account == "no":
                self.login()
            elif account == "y" or account == "Y" or account == "yes":
                self.create_account()

    def create_quizz(self):
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

        file.write(f"{self.logged_user}\n")

        for i in range(num_questions):
            file.write(f"{questions[i]},{answers[i]},{correct_answers[i]},{points[i]}\n")

        file.close()

        print(f"Quizz has been saved to {os.path.abspath(file_name)}.")

quizzer()