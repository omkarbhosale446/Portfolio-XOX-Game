# to-do 1
# To play this game first we need to have a 3x3 box. Another challenge here is to save a data in those boxes. For that
# we will use dictionary which will have keys as position of of box initially empty values which we will fill as per
# user wish.

box_data = {
    "1" : " ", "2" : " ", "3" : " ",
    "4" : " ", "5" : " ", "6" : " ",
    "7" : " ", "8" : " ", "9" : " "
    }

box_values = []

for value in box_data:
    box_values.append(value)

# to-do "2"
# We need some sort of layout like a cells in sheet, which can help us distinguish between cells

def box_layout(box):
    print(box["1"] + "|" + box["2"] + "|" + box["3"])
    print("-+-+-")
    print(box["4"] + "|" + box["5"] + "|" + box["6"])
    print("-+-+-")
    print(box["7"] + "|" + box["8"] + "|" + box["9"])



# to-do "3"
# Here we need to have some backend of the game. Here we will check a the given input is right or not
# We also need to check which player has won the game.
# We need to check which player has won.
# We also want to switch players.
# We also want to restart the game once it's gets finished.


def gameplay():

    chance = "X"
    score = 0

    for i in range(10):
        box_layout(box_data)
        print(f"Now {chance} choose the place to mark.")

        move = input()

        if box_data[move] == " ":
            box_data[move] = chance
            score += 1

        else:
            print("We can't go to already filled space. Select another. \n")
            continue

        if score >= 5:
            if box_data["7"] == box_data["8"] == box_data["9"] != " ":
                box_layout(box_data)
                print("GAME OVER")
                print(f"Hurray!!!!!!!*******{chance} won!!!!!!******")
                break

            elif box_data["4"] == box_data["5"] == box_data["6"] != " ":
                box_layout(box_data)
                print("GAME OVER")
                print(f"Hurray!!!!!!!*******{chance} won!!!!!!******")
                break

            elif box_data["1"] == box_data["2"] == box_data["3"] != " ":
                box_layout(box_data)
                print("GAME OVER")
                print(f"Hurray!!!!!!!*******{chance} won!!!!!!******")
                break

            elif box_data["1"] == box_data["4"] == box_data["7"] != " ":
                box_layout(box_data)
                print("GAME OVER")
                print(f"Hurray!!!!!!!*******{chance} won!!!!!!******")
                break

            elif box_data["2"] == box_data["5"] == box_data["8"] != " ":
                box_layout(box_data)
                print("GAME OVER")
                print(f"Hurray!!!!!!!*******{chance} won!!!!!!******")
                break

            elif box_data["3"] == box_data["6"] == box_data["9"] != " ":
                box_layout(box_data)
                print("GAME OVER")
                print(f"Hurray!!!!!!!*******{chance} won!!!!!!******")
                break

            elif box_data["1"] == box_data["5"] == box_data["9"] != " ":
                box_layout(box_data)
                print("GAME OVER")
                print(f"Hurray!!!!!!!*******{chance} won!!!!!!******")
                break
            elif box_data["3"] == box_data["5"] == box_data["7"] != " ":
                box_layout(box_data)
                print("GAME OVER")
                print(f"Hurray!!!!!!!*******{chance} won!!!!!!******")
                break

        if score == 9:
            print("GAME OVER")
            print("***************** It's 👔 !! ********")

        if chance == "X":
            chance = "O"
        else:
            chance = "X"



    restart = input("Wish to play again?(y/n):").lower()
    if restart == "y":
        for value in box_values:
            box_layout[value] = " "


        gameplay()

gameplay()
