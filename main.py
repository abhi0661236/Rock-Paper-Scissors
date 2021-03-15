import random
import tkinter as tk

# creating a window
window = tk.Tk()
window.geometry("244x250")
window.title("Rock-Paper-Scissor Game")

# Creating some superglobals
USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

def choice_to_number(choice):
    rps = {"rock":0,"paper":1,"scissor":2};
    return rps[choice]

def number_to_choice(number):
    rps = {0:'rock',1:'paper',2:'scissor'}
    return rps[number]

def random_computer_choice():
    return random.choice(['rock','paper','scissor'])

def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)

    if user==comp:
        print("Tie")
    elif (user-comp)%3==1:
        print("You won !")
        USER_SCORE += 1
    else:
        print("You Lose !")
        COMP_SCORE += 1

    text_aria = tk.Text(master=window, height=12, width=30, bg ='#aaaaaa')
    text_aria.grid(column=1, row=4)
    answer = "Your choice: {uc} \nComputer's choice: {cc} \nYour score: {u} \nComputer's score: {c}".format(uc=USER_CHOICE, cc=COMP_CHOICE, u=USER_SCORE, c=COMP_SCORE)
    text_aria.insert(tk.END, answer)


def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'rock'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'paper'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)
def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = 'scissor'
    COMP_CHOICE = random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)


button1 = tk.Button(text="Rock", bg="skyblue", command=rock, width = 10)
button1.grid(column=1,row=1)

button2 = tk.Button(text="Paper", bg="pink", command=paper, width=10)
button2.grid(column=1,row=2)

button3 = tk.Button(text="Scissor", bg="green", command=scissor, width=10)
button3.grid(column=1,row=3)

window.mainloop()