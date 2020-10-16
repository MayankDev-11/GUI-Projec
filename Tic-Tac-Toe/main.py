from tkinter import *
from tkinter import ttk
import random
import time
from tkinter import messagebox

root = Tk()
root.geometry("500x125")
root.resizable(0,0)
root.iconbitmap("img.ico")

Label_Font = ("SimSun",16)

user_frame = ttk.Frame(root)
user_frame.pack(padx = 16,pady = (16,8))
game_frame = ttk.Frame(root)
game_frame.pack(padx = 16,pady = (8,16))

name_frame1 = Frame(root)
game_frame1 = Frame(root)

input_frame = Frame(root)
output_frame = Frame(root)
label_frame = Frame(root)

count = 0

def exitFunc():
    root.destroy()

def reset():
    global a
    global count
    a = 1
    count = 0
    button1['text'] = ""
    button2['text'] = ""
    button3['text'] = ""
    button4['text'] = ""
    button5['text'] = ""
    button6['text'] = ""
    button7['text'] = ""
    button8['text'] = ""
    button9['text'] = ""

def button_func(number):
    global a
    global count

    if number == 1 and button1['text'] == "" and a == 1:
        button1['text'] = "X"
        a = 0
        Descision = root.after(500,lambda : ttk.Label(input_frame, text = f"{secondPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0))
        count += 1

    if number == 1 and button1['text'] == "" and a == 0:
        button1['text'] = "O"
        input_frame.pack_forget()
        label_frame.pack(padx = 16,pady = (8,16))
        a = 1
        Descision = root.after(500,lambda : ttk.Label(label_frame, text = f"{firstPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0))
        count += 1

    if number == 2 and button2['text'] == "" and a == 1:
        button2['text'] = "X"
        label_frame.pack_forget()
        input_frame.pack(padx = 16,pady = (8,16))
        a = 0
        Descision = root.after(500,lambda : ttk.Label(input_frame, text = f"{secondPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1

    if number == 2 and button2['text'] == "" and a == 0:
        button2['text'] = "O"
        input_frame.pack_forget()
        label_frame.pack(padx = 16,pady = (8,16))
        a = 1
        Descision = root.after(500,lambda : ttk.Label(label_frame, text = f"{firstPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1
    
    if number == 3 and button3['text'] == "" and a == 1:
        button3['text'] = "X"
        label_frame.pack_forget()
        input_frame.pack(padx = 16,pady = (8,16))
        a = 0
        Descision = root.after(500,lambda : ttk.Label(input_frame, text = f"{secondPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1

    if number == 3 and button3['text'] == "" and a == 0:
        button3['text'] = "O"
        input_frame.pack_forget()
        label_frame.pack(padx = 16,pady = (8,16))
        a = 1
        Descision = root.after(500,lambda : ttk.Label(label_frame, text = f"{firstPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1
    
    if number == 4 and button4['text'] == "" and a == 1:
        button4['text'] = "X"
        label_frame.pack_forget()
        input_frame.pack(padx = 16,pady = (8,16))
        a = 0
        Descision = root.after(500,lambda : ttk.Label(input_frame, text = f"{secondPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1

    if number == 4 and button4['text'] == "" and a == 0:
        button4['text'] = "O"
        input_frame.pack_forget()
        label_frame.pack(padx = 16,pady = (8,16))
        a = 1
        Descision = root.after(500,lambda : ttk.Label(label_frame, text = f"{firstPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1
    
    if number == 5 and button5['text'] == "" and a == 1:
        button5['text'] = "X"
        label_frame.pack_forget()
        input_frame.pack(padx = 16,pady = (8,16))
        a = 0
        Descision = root.after(500,lambda : ttk.Label(input_frame, text = f"{secondPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1

    if number == 5 and button5['text'] == "" and a == 0:
        button5['text'] = "O"
        input_frame.pack_forget()
        label_frame.pack(padx = 16,pady = (8,16))
        a = 1
        Descision = root.after(500,lambda : ttk.Label(label_frame, text = f"{firstPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1
        
    if number == 6 and button6['text'] == "" and a == 1:
        button6['text'] = "X"
        label_frame.pack_forget()
        input_frame.pack(padx = 16,pady = (8,16))
        a = 0
        Descision = root.after(500,lambda : ttk.Label(input_frame, text = f"{secondPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1

    if number == 6 and button6['text'] == "" and a == 0:
        button6['text'] = "O"        
        input_frame.pack_forget()        
        label_frame.pack(padx = 16,pady = (8,16))
        a = 1
        Descision = root.after(500,lambda : ttk.Label(label_frame, text = f"{firstPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1
    
    if number == 7 and button7['text'] == "" and a == 1:
        button7['text'] = "X"
        label_frame.pack_forget()
        input_frame.pack(padx = 16,pady = (8,16))
        a = 0
        Descision = root.after(500,lambda : ttk.Label(input_frame, text = f"{secondPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1

    if number == 7 and button7['text'] == "" and a == 0:
        button7['text'] = "O"
        input_frame.pack_forget()
        label_frame.pack(padx = 16,pady = (8,16))
        a = 1
        Descision = root.after(500,lambda : ttk.Label(label_frame, text = f"{firstPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1
    
    if number == 8 and button8['text'] == "" and a == 1:
        label_frame.pack_forget()
        button8['text'] = "X"
        input_frame.pack(padx = 16,pady = (8,16))
        a = 0
        Descision = root.after(500,lambda : ttk.Label(input_frame, text = f"{secondPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1

    if number == 8 and button8['text'] == "" and a == 0:
        button8['text'] = "O"
        input_frame.pack_forget()
        label_frame.pack(padx = 16,pady = (8,16))
        a = 1
        Descision = root.after(500,lambda : ttk.Label(label_frame, text = f"{firstPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1
    
    if number == 9 and button9['text'] == "" and a == 1:
        label_frame.pack_forget()
        button9['text'] = "X"
        input_frame.pack(padx = 16,pady = (8,16))
        a = 0
        Descision = root.after(500,lambda : ttk.Label(input_frame, text = f"{secondPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1

    if number == 9 and button9['text'] == "" and a == 0:
        button9['text'] = "O"
        input_frame.pack_forget()
        label_frame.pack(padx = 16,pady = (8,16))
        a = 1
        Descision = root.after(500,lambda : ttk.Label(label_frame, text = f"{firstPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0)) 
        count += 1


    # Winner Descision

    if (button1['text'] == "X" and button2['text'] == "X" and button3['text'] == "X" or
        button4['text'] == "X" and button5['text'] == "X" and button6['text'] == "X" or
        button7['text'] == "X" and button8['text'] == "X" and button9['text'] == "X" or
        button1['text'] == "X" and button4['text'] == "X" and button7['text'] == "X" or
        button2['text'] == "X" and button5['text'] == "X" and button8['text'] == "X" or
        button3['text'] == "X" and button6['text'] == "X" and button9["text"] == "X" or
        button1['text'] == "X" and button5['text'] == "X" and button9["text"] == "X" or
        button3['text'] == "X" and button5['text'] == "X" and button7['text'] == "X"):

        playAgain = messagebox.askquestion("Winner!!",f"Congo!{firstPlayer} has won the game.Do you want to play again?",icon = "img.ico")
        if playAgain == "yes":
            reset()
        else:
            exitFunc()

    if (button1['text'] == "O" and button2['text'] == "O" and button3['text'] == "O" or
        button4['text'] == "O" and button5['text'] == "O" and button6['text'] == "O" or
        button7['text'] == "O" and button8['text'] == "O" and button9['text'] == "O" or
        button1['text'] == "O" and button4['text'] == "O" and button7['text'] == "O" or
        button2['text'] == "O" and button5['text'] == "O" and button8['text'] == "O" or
        button3['text'] == "O" and button6['text'] == "O" and button9["text"] == "O" or
        button1['text'] == "O" and button5['text'] == "O" and button9["text"] == "O" or
        button3['text'] == "O" and button5['text'] == "O" and button7['text'] == "O"):


        playAgain1 = messagebox.askquestion("Winner!!",f"Congo!{secondPlayer} has won the game.Do you want to play again?")
        if playAgain1 == "yes":
            reset()
        else:
            exitFunc()

    if (count == 9):
        
        playAgain2 = messagebox.askquestion("Draw!!",f"There is a draw!!Do you want to play again?")
        if playAgain2 == "yes":
            reset()
        else:
            exitFunc()

def wish():
    global Greeting
    Greeting = ttk.Label(user_frame,font = Label_Font,text = "Hey there").grid(row = 0,column = 0)
    Greeting2 = ttk.Label(user_frame,text = "Welcome to the TIC-TAC-TOE Game!!",font = Label_Font).grid(row = 1,column = 0)


def main():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global players
    global firstPlayer
    global Descision
    global secondPlayer
    global a

    a = 1

    player2 = name2.get()
    name_frame1.destroy()
    game_frame1.destroy()

    root.geometry("370x300")
    input_frame.pack(padx = 16,pady = (8,16))
    output_frame.pack(padx = 16,pady = (16,8))

    players = [player1,player2]
    firstPlayer = random.choice(players)

    for i in range(len(players)):
        if players[i] != firstPlayer:
            secondPlayer = players[i]

    ttk.Label(input_frame,text = f"{firstPlayer} will play first.",font = Label_Font).grid(row = 0,column = 0)

    Descision = root.after(1000,lambda : ttk.Label(input_frame, text = f"{firstPlayer} please make your move!!",font = Label_Font).grid(row = 0,column =0))

    button1 = ttk.Button(output_frame,width=10,command =lambda:button_func(1))
    button1.grid(row = 0,column =0, ipady=20, ipadx=10)
    
    button2 = ttk.Button(output_frame,width = 10,command = lambda:button_func(2))
    button2.grid(row = 0,column =1, ipady = 20,ipadx = 10)
    
    button3 = ttk.Button(output_frame,width =10,command =lambda:button_func(3))
    button3.grid(row = 0,column =2,ipady = 20,ipadx = 10)
    
    button4 = ttk.Button(output_frame,width =10,command =lambda:button_func(4))
    button4.grid(row = 1,column =0, ipady = 20,ipadx = 10)

    button5 = ttk.Button(output_frame,width =10,command = lambda:button_func(5))
    button5.grid(row =1,column = 1, ipady = 20,ipadx = 10)

    button6 = ttk.Button(output_frame,width =10,command =lambda:button_func(6))
    button6.grid(row =1,column =2,ipady = 20,ipadx = 10)

    button7 = ttk.Button(output_frame,width =10,command = lambda:button_func(7))
    button7.grid(row =2,column =0, ipady = 20, ipadx = 10)

    button8 = ttk.Button(output_frame,width = 10,command = lambda:button_func(8))
    button8.grid(row =2,column =1,ipady = 20,ipadx = 10)

    button9 = ttk.Button(output_frame,width = 10,command = lambda:button_func(9))
    button9.grid(row =2,column = 2,ipady = 20,ipadx = 10)

def names():
    global player1
    global name2

    player1 = name1.get()
    name1.delete(0,END)
    game_frame.destroy()
    name_frame.destroy()
    name_frame1.pack(padx = 16,pady = (16,8))
    game_frame1.pack(padx = 16,pady = (8,16))

    ttk.Label(name_frame1, text = "Please enter the second player name:",font = Label_Font).grid(row = 0,column =0)    
    name2 = ttk.Entry(game_frame1,font = 40)
    name2.grid()

    submit_name2 = ttk.Button(game_frame1,command = main,text = "Submit")
    submit_name2.grid(padx = 10)



def Names():
    global name1 
    global name_frame
    user_frame.destroy()
    name_frame = ttk.Frame(root)
    name_frame.pack(padx = 16,pady = (16,8))

    ttk.Label(game_frame, text = "Please enter the first player name:",font = Label_Font).grid(row = 0,column =0)    
    name1 = ttk.Entry(name_frame,font = 40)
    name1.grid()
    submit_name1 = ttk.Button(name_frame,command = names,text = "Submit")
    submit_name1.grid(padx = 10)

wish()


root.after(2000,lambda:Names())
Name1 = None

root.mainloop()