import random as rd

print("*"*60)
print("\t\tWELCOME TO THE QUIZ")
print("*"*60)
name = input("Enter your name:")
print("Here are the rules of the game: \nYou will be given 1 point for each correct answer and for each wrong answer 0 point wil be given")
quiz = int(input("You have two subject to play the game:\nPress 1 to play Maths quiz\nPress 2 to play GK quiz\nEnter your choice:"))
if quiz == 1:

    num = int(input("Enter how many times you want to play the game:"))
    print("All the best",name,"!!!")
    c = 0
    for i in range (num):
        num1 = rd.randint(1,20)
        num2 = rd.randint(1,20)
    
        a =["*","-","+","//"]
        b = rd.choice(a)
        print(num1,b,num2)
        inp = int(input("Enter your answer"))
        
        if b == "*":
            if inp == num1 * num2:
                print("Correct answer!!!")
                c += 1
                print("You scored 1 point")
            else:
                print("wrong answer")
                c += 0
        if b == "+":
            if inp == num1 + num2:
                print("Correct answer!!!")
                c += 1
                print("You scored 1 point")
            else:
                print("wrong answer")
        if b == "-":
            if inp == num1 - num2:
                print("Correct answer!!!")
                c += 1
                print("You scored 1 point")
            else:
                print("wrong answer")
        if b == "//":
             if inp == num1 // num2:
                print("Correct answer!!!")
                c += 1
                print("Your scored 1 point")
             else:
                print("Wrong answer")
        

if quiz == 2:
    num = int(input("Enter how many times you want to play:"))
    print("All the best",name,"!!!")
    c = 0
    ques = ["Who is current prime minister of India?","What is Fulll form of A.I.?","How many keywords for loops are there in python?","What is the name of highest statue in the world ?","Only language that uses compiler as well as interpreter?","if 6 = 32,\n5 = 27,\n7 = 37,\n8 = ?"] 
    ans = ["Mr.Narendra Modi","Artificial Intelligence","2","Statue Of Unity","Java","42"]
    for j in range(num):
        a = rd.choice(ques)
        print(a)
        inp = input("Enter your answer:")
        
        for i in range(len(ans)):
            if inp.title() == ans[i]:
                print("Correct answer")
                c += 1
                print("You scored 1 point")
                break
        else:
            print("Wrong answer")

print("-"*60)
print("\t\tYOUR SCORE IS",c,"/",num)
if c == num or c >= num-1:
    print("\n\t\tAmazing performance!!!")
elif c < num-3 or c > num-4:
    print("\t\tWell done!!")
print("*"*60)
print("\t\tThank You For Playing :)")
print("*"*60)            
 
