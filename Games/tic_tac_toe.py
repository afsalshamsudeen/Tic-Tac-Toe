from tkinter import *
import random

def next_turn(row,column):

# this function states the switching of turns to next user

    global player

    if buttons[row][column]['text']=="" and check_winner() is False:

        if player==players[0]:
            buttons[row][column]['text']=player

            if check_winner() is False:
                player=players[1]
                label.config(text=(players[1]+" turn"))
            
            elif check_winner() is True:
                label.config(text=(player[0]+" wins"))
            elif check_winner() =="Tie!!!":
                label.config(text="Tie!!!",font="consoles")
            
        else:
            buttons[row][column]['text']=player

            if check_winner() is False:
                player=players[0]
                label.config(text=(players[0]+" turn"))
            
            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))
            elif check_winner() =="Tie!!!":
                label.config(text="Tie!!!",font="consoles")



def check_winner():

#this function is to check the winner of game
#which includes which row or column is filles
#cross,vertical,horizontal
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] !="":
            buttons[row][0].config(bg="#95EE45")
            buttons[row][1].config(bg="#95EE45")
            buttons[row][2].config(bg="#95EE45")
            return True
        
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] !="":
            buttons[0][column].config(bg="#95EE45")
            buttons[1][column].config(bg="#95EE45")
            buttons[2][column].config(bg="#95EE45")
            return True
            
    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text'] !="":
        buttons[0][0].config(bg="#95EE45")
        buttons[1][1].config(bg="#95EE45")
        buttons[2][2].config(bg="#95EE45")
        return True
    
    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text'] !="":
        buttons[0][2].config(bg="#95EE45")
        buttons[1][1].config(bg="#95EE45")
        buttons[2][0].config(bg="#95EE45")
        return True

    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#F0FF28")

        return "Tie!!!"
    else:
        # for row in range(3):
        #     for column in range(3):
        #         buttons[row][column].config(bg="yellow")
        return False

def empty_spaces():

#this function deals with the empty spaces in the board |which is the unchecked cubes

    spaces =9

    for  row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] !="": 
                spaces-=1
    if spaces == 0:
       
        return False
    else:
        return True

def new_game():
    global player

    player =random.choice(players)
    label.config( text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

#This is the windows section###################################################################################
window=Tk()
window.geometry("450x450")
window.title("Tic-Tac-Toe")
window.config(bg="#A095E4")
print("PROGRAM EXECUTED SUCCESSFULLY!!!!!!!!!")


players=["x","o"]
player=random.choice(players)
buttons=[[0,0,0],
        [0,0,0],
        [0,0,0]]

label=Label(text=player+"turn")
label.pack(side="top")

#The Reset button!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
reset_button=Button(text="restart",width=15,height=1,bg="#FFB859",font="consoles",command=new_game)
reset_button.pack(side="top")

frame=Frame(window)
frame.pack()

#main butttons to play %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
for row in range(3):
    for column in range(3):
        buttons[row][column]=Button(frame,text="",font='consoles',width=5,height=5,command=lambda row=row,column=column:next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)
window.mainloop()