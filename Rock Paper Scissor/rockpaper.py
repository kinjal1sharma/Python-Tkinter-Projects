import random
import tkinter as ttk 

#Lets create a window
window = ttk.Tk()
window.geometry("400x300")
window.title("Rock Paper Scissors Game") 

#Defining Variables

USER_SCORE= 0
COMP_SCORE= 0
USER_CHOICE = ""
COMP_CHOICE = "" 


#Methods for converting the user's choice to a number

def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissor':2}
    return rps[choice]
def number_to_choice(number):
    rps={0:'rock',1:'paper',2:'scissor'}
    return rps[number]

#function to get the computers choice

def random_computer_choice():
    return random.choice(['rock','paper','scissor']) 


#result function
def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You win")
        USER_SCORE+=1
    else:
        print("Comp wins")
        COMP_SCORE+=1

    #look of the window 
    text_area = ttk.Text(master=window,height=14,width=80,bg="#FFFF99")
    text_area.grid(column=0,row=5)
    answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(uc=USER_CHOICE,cc=COMP_CHOICE,u=USER_SCORE,c=COMP_SCORE)    
    text_area.insert(ttk.END,answer)


#methods for different user choice
def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE,COMP_CHOICE)
def scissor():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissor'
    COMP_CHOICE=random_computer_choice() 
    result(USER_CHOICE,COMP_CHOICE)



#Building Buttons
button1 = ttk.Button(text="       Rock       ",bg="skyblue",command=rock)
button1.grid(column=0,row=1)
button2 = ttk.Button(text="       Paper      ",bg="pink",command=paper)
button2.grid(column=0,row=2)
button3 = ttk.Button(text="      Scissor     ",bg="lightgreen",command=scissor)
button3.grid(column=0,row=3)

window.mainloop()