import random as rd

print("<>" * 30)
print('\t\t\tONLINE XO ')
print("<>" * 30)
grid = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}


def show():
    print("-" * 15)
    print(" | " + grid[1] + " | " + grid[2] + " | " + grid[3] + " | ")
    print("-" * 15)
    print(" | " + grid[4] + " | " + grid[5] + " | " + grid[6] + " | ")
    print("-" * 15)
    print(" | " + grid[7] + " | " + grid[8] + " | " + grid[9] + " | ")
    print("-" * 15)


def Complayer():
    player1 = input("Enter player 1 name :")
    turn = 1
    while True:
        print("*" * 20)
        show()
        if turn % 2 == 1:
            pos = int(input(player1 + " enter the position to fill X :"))
            if grid[pos] == " " and pos in grid:
                grid[pos] = "X"
                turn += 1
        else:
            pos = rd.randint(1, 9)
            if grid[pos] == " " and pos in grid:
                grid[pos] = "0"
                turn += 1

        # Deciding winner
        if grid[1] == grid[2] == grid[3] and grid[1] != " ":
            if grid[1] == "X":
                print(player1, "wins")
            else:
                print("Computer wins")
            show()
            break

        elif grid[4] == grid[5] == grid[6] and grid[4] != " ":
            if grid[4] == "X":
                print(player1, "wins")
            else:
                print("Computer wins")
            show()
            break
        elif grid[7] == grid[8] == grid[9] and grid[7] != " ":
            if grid[7] == "X":
                print(player1, "wins")
            else:
                print("Computer wins")
            show()
            break
        elif grid[1] == grid[5] == grid[9] and grid[1] != " ":
            if grid[1] == "X":
                print(player1, "wins")
            else:
                print("Computer wins")
            show()
            break
        elif grid[3] == grid[5] == grid[7] and grid[7] != " ":
            if grid[7] == "X":
                print(player1, "wins")
            else:
                print("Computer wins")
            show()
            break
        elif grid[1] == grid[4] == grid[7] and grid[1] != " ":
            if grid[1] == "X":
                print(player1, "wins")
            else:
                print("Computer wins")
            show()
            break
        elif grid[2] == grid[5] == grid[8] and grid[2] != " ":
            if grid[2] == "X":
                print(player1, "wins")
            else:
                print("Computer wins")
            show()
            break
        elif grid[3] == grid[6] == grid[9] and grid[3] != " ":
            if grid[3] == "X":
                print(player1, "wins")
            else:
                print("Computer wins")
            show()
            break
        elif turn > 9:
            print("Game draw")
            show()
            break


def Players():
    player1 = input("Enter player 1 name :")
    player2 = input("Enter player 2 name :")
    turn = 1
    while True:
        show()
        if turn % 2 == 1:
            pos = int(input(player1 + " enter the position to fill X :"))
            if grid[pos] == " " and pos in grid:
                grid[pos] = "X"
                turn += 1
        else:
            pos = int(input(player2 + " enter the position to fill 0 :"))
            if grid[pos] == " " and pos in grid:
                grid[pos] = "0"
                turn += 1

        # Deciding winner
        if grid[1] == grid[2] == grid[3] and grid[1] != " ":
            if grid[1] == "X":
                print(player1, "wins")
            else:
                print(player2, "wins")
            show()
            break

        elif grid[4] == grid[5] == grid[6] and grid[4] != " ":
            if grid[4] == "X":
                print(player1, "wins")
            else:
                print(player2, "wins")
            show()
            break
        elif grid[7] == grid[8] == grid[9] and grid[7] != " ":
            if grid[7] == "X":
                print(player1, "wins")
            else:
                print(player2, "wins")
            show()
            break

        elif grid[1] == grid[5] == grid[9] and grid[1] != " ":
            if grid[1] == "X":
                print(player1, "wins")
            else:
                print("Computer wins")
            show()
            break
        elif grid[3] == grid[5] == grid[7] and grid[7] != " ":
            if grid[7] == "X":
                print(player1, "wins")
            else:
                print("Computer wins")
            show()
            break
        elif grid[1] == grid[4] == grid[7] and grid[1] != " ":
            if grid[1] == "X":
                print(player1, "wins")
            else:
                print(player2, "wins")
            show()
            break
        elif grid[2] == grid[5] == grid[8] and grid[2] != " ":
            if grid[2] == "X":
                print(player1, "wins")
            else:
                print(player2, "wins")
            show()
            break
        elif grid[3] == grid[6] == grid[9] and grid[3] != " ":
            if grid[3] == "X":
                print(player1, "wins")
            else:
                print(player2, "wins")
            show()
            break
        elif turn > 9:
            print("Game draw")
            show()
            break

while True:
    print("PRESS 1 - PLAY WITH COMPUTER ")
    print("PRESS 2 - PLAY WITH FRIENDS ")
    ch = int(input("Enter your choice :"))
    if ch == 1:
        grid = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
        Complayer()
    elif ch == 2:
        grid = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
        Players()
    ask = input("Do you want to play again (yes/no) :")
    if ask.lower() == 'no':
        break
