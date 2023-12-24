#importing Libraries : tkinter, csv, random, datetime
#Backend used is file handling: CSV File
from tkinter import *
import csv
import random as rd
from datetime import datetime
#creating window for tkinter
win = Tk()
win.geometry("525x400")
parent = win.title("GUESS THE NUMBER GAME") #creating title for the window
a = rd.randint(1, 100)
c = 0
name = ""
d = {}
#creating guess function to guess the, giving hints, adding data in CSV File
def Guess():
    global name
    name = str(e1.get()) #explicitly converting name to string datatype
    global c
    c = c + 1
    if c <= 7:
        ask = int(e4.get())
        if ask == a:
            l5.configure(text="Congratulations "+ name + " YOU WIN !!!")
            # Creating CSV File and adding data of Players
            pts = (7 - c) * 10 + 1
            f = open("new.csv", "a")
            wr = csv.writer(f)
            data = [name.lower(), str(pts), datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
            wr.writerow(data) #adding data in CSV file
            f.close()
        elif ask > a:
            l5.configure(text="The number is smaller than your guess\n")
        elif ask < a:
            l5.configure(text="The number is greater than your guess\n")
        e4.delete(0,END)
    else:
        l5.configure(text="OOh! BETTER LUCK NEXT TIME !!! "
                          "The number was "+str(a))
        # Creating CSV File and adding data of Players
        pts = 0
        f = open("new.csv", "a")
        wr = csv.writer(f)
        data = [name.lower(), str(pts), datetime.now().strftime('%Y-%m-%d %H:%M:%S')]
        wr.writerow(data)
        f.close()
#creating function to calculate highest points
def highest_points():
    max = 0
    l5.configure(text="SHOWING POINTS")
    f = open("new.csv","r")
    cr = csv.reader(f)
    for i in cr:
        if len(i) == 0:
            continue
        else:
            if i[0] not in d:
                d[i[0]] = int(i[1])
            else:
                d[i[0]] += int(i[1])
    for j in d:
        if int(d[j]) > max:
            max = d[j]
            name = j


    l5.configure(text="Highest points are scored by "+name)

    f.close()

#creating function to search a player and show its points
def search():
    name = str(e1.get())
    f = open("new.csv","r") #opening csv file
    cr = csv.reader(f)
    points = 0
    for i in cr:
        if len(i) == 0:
            continue
        else:
            if i[0].lower() == name.lower():
                points += int(i[1]) #calculating total points
    l5.configure(text=name+"'s total points are "+str(points))
    f.close()

#Creating Labels, Buttons, Entries for user inputs
win['background'] = "black"
l1 = Label(win,text=" WELCOME TO GUESS THE NUMBER GAME",bg = "black",fg = "#2E8BC0") #Creating Labels
l1.place(x=130,y=50)
l2 = Label(win,text="Enter Name : ",bg = "black",fg = "white")
l2.place(x=30,y=120)
e1 = Entry(win,text="Enter Name")                                                #creating entry for name
e1.place(x=120,y=120)
l4 = Label(win,text="Guess a number between 1 and 100",bg = "black",fg = "white")
l4.place(x=30,y=170)
e4 = Entry(win)
e4.place(x=30,y=190)

#creating button for guessing number
b1 = Button(win,text="Guess",command=Guess,bg = "red",fg = "white")
b1.place(x=50,y=230)
l5 = Label(win,text="Your Guess Result",bg = "black",fg = "yellow")
l5.place(x=180,y=270)

#making menu
mb = Menu(win)
win.config(menu=mb)
m1 = Menu(mb)
m1.add_command(label="Highest points",command=highest_points)
m1.add_command(label="Search",command=search)
mb.add_cascade(label="Functions",menu=m1,underline=2)

win.mainloop()
