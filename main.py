import random
import  gui
# import gui2
import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import messagebox

count = 0
num_of_quiz = 0

while True:
    gui.display_image(count)
    age_group = input("Choose your age group: \nA: 6-8 \nB: 9-10 \nC: 11-12")
    if age_group == 'A' or age_group == 'B' or age_group == 'C':
        break
    else:
        print("Invalid input.")



if age_group == "A":
    while count<10 and num_of_quiz<25:
      a, b= random.randint(1,100), random.randint(1,100)
      num_of_quiz += 1
      random_boolean = random.choice([True, False])
      if random_boolean:
        answer = input(f"{a} + {b} = ")
        if answer != str(a+b):
            count = count + 1
            print(count)

            gui.display_image(count)
            print("wrong answer")

        else:
            print("Correct!")
      else:
        answer = input(f"{a} - {b} = ")
        if answer != str(a - b):
            count = count + 1
            print("wrong answer")
            gui.display_image(count)
        else:
            print("Correct!")


elif age_group == "B":
    while count<10 and num_of_quiz<25:
        num_of_quiz +=1
        random_boolean = random.choice([True,False])
        if random_boolean:
            a, b = random.randint(-50, 50), random.randint(-50, 50)
            answer = input(f"{a} * {b} = ")
            if answer != str(a*b):
                count = count +1
                print ("wrong answer")
                gui.display_image(count)
            else:
                print("Correct!")
        else:
            b,n = random.randint(1,10), random.randint(1,10)
            a = b*n
            answer = input(f"{a} / {b} = ")
            if answer != str(n):
                count = count + 1
                print("wrong answer")
                gui.display_image(count)
            else:
                print("Correct!")

else:
    gui.display_image(count)
    while count<10 and num_of_quiz<25:
        a,b,c,x = random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)
        while a*x + b != c:
            a, b, c, x = random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)
        num_of_quiz += 1
        answer = input(f"What is x for equation:{a} *x + {b} = {c} ")
        if answer != str(x):
            count = count + 1
            print("wrong answer")
            gui.display_image(count)
        else:
            print("Correct!")



