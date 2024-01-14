import tkinter as tk
from tkinter import *
import random

pause = False
USER_SCORE = 0
COMP_SCORE = 0


main = tk.Tk()
main.title('Rock paper and Scissor game')

window_width = 1000
window_height = 400

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

# Center point
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

main.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


computer_choice = {
    "0" : "Rock",
    "1" : "Paper",
    "2" : "Scissor"
}

#Disable all the Buttons after first Match
# Disable the Button
def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"

#if the user chose Rock
def user_rock (): 
    global USER_SCORE
    global COMP_SCORE
    comp_choice = computer_choice[str(random.randint(0,2))]
    if comp_choice == "Rock":
        result = ("It is a tie, you may win next round")
    elif comp_choice == "Paper":
        result = ("Paper cover Rock. You lose. Don't cry :( ")
        COMP_SCORE += 1
    else :
        result = ("Rock smach the Scissor. Wow, Congratulation. You are a genius! ")
        USER_SCORE += 1
        
    label.config(text = result)
    l1.config(text = "Rock")
    l3.config(text = comp_choice)
    l5.config(text = f"User Score: {USER_SCORE}")
    l6.config(text= f" Computer Score: {COMP_SCORE}")
    button_disable()

#if the user chose Papar
def user_paper ():
    global USER_SCORE
    global COMP_SCORE
    comp_choice = computer_choice[str(random.randint(0,2))]
    if comp_choice == "Paper":
        result = ("It is a tie, try harder to win :) ")
    elif comp_choice == "Scissor":
        result = ("Scissor cut the Paper. Sorry, try harder next round.")
        COMP_SCORE +=1
    else:
        result = ("Paper cover Rock. Awesome, You win.")
        USER_SCORE +=1
    label.config(text = result)
    l1.config(text = "Paper")
    l3.config(text = comp_choice)
    l5.config(text = f"User Score: {USER_SCORE}")
    l6.config(text= f" Computer Score: {COMP_SCORE}")
    button_disable()

# if the user chose Scissor
def user_scissor ():
    global USER_SCORE
    global COMP_SCORE
    comp_choice = computer_choice[str(random.randint(0,2))]
    if comp_choice == "Scissor":
        result = ("It is a tie, try your best to win next round")
    elif comp_choice == "Paper":
        result = ("Scissor cut the Paper. You Win, keep winning next round!")
        USER_SCORE += 1
    else :
        result = ("Rock smach the Scissor. Unfortunately, You lose.")
        COMP_SCORE += 1
    label.config(text = result)
    l1.config(text = "Scissor")
    l3.config(text = comp_choice)
    l5.config(text = f"User Score: {USER_SCORE}")
    l6.config(text= f" Computer Score: {COMP_SCORE}")
    button_disable()

#Reset the Game
# Reset The Game
def reset_game():
	b1["state"] = "active"
	b2["state"] = "active"
	b3["state"] = "active"
	l1.config(text = "Player")
	l2.config(text = "Vs")
	l3.config(text = "Computer")
    

#Create a LabelFrame
labelframe= LabelFrame(main, text= "Rock Paper Scissor Game", font= ('Century 40 bold'),labelanchor= "n",bd=5,bg= "lightyellow",width= 600, height= 450, cursor= "spider")
labelframe.pack(expand= True, fill= BOTH)

#Label for Player
l1= Label(labelframe, text="Player", font= ("Times", "24"), bg = "khaki", fg = "teal")
l1.place(relx= .18, rely= .1)

#Label for Score 
l5 = Label(labelframe, text= "", font= ("Times", "12"), bg="lightyellow", fg = "red")
l5.place(relx= .03, rely= .8)
l6 = Label(labelframe, text= "", font= ("Times", "12"), bg="lightyellow", fg = "red")
l6.place(relx= .03, rely= .9)


#Label for VS
l2= Label(labelframe, text="VS", font= ("Times", "24"), bg="lightyellow", fg = "red")
l2.place(relx= .45, rely= .1)

#Label for Computer
l3= Label(labelframe, text="Computer", font= ("Times", "24"), bg = "khaki", fg = "teal")
l3.place(relx= .65, rely= .1)

#Create a label to display the Conditions
label= Label(labelframe, text="", font=('Coveat', 25,'bold'), bg= "lightyellow")
label.pack(pady=150)

#Create Button Set for Rock, Paper and Scissor
b1= Button(labelframe, text= "Rock", font= 10, width= 7, command= user_rock, fg="blueviolet")
b1.place(relx=.25, rely= .62)
b2= Button(labelframe, text= "Paper", font= 10, width= 7 ,command= user_paper, fg="seagreen")
b2.place(relx= .41,rely= .62)
b3= Button(labelframe, text= "Scissor", font= 10, width= 7, command= user_scissor, fg="darkorange")
b3.place(relx= .58, rely= .62)

# Button to reset the Game
reset= Button(labelframe, text= "Reset",bg= "OrangeRed3", fg = "dodgerblue",width= 7, font= 10, command= reset_game)
reset.place(relx= .8, rely= .62)

main.mainloop()




