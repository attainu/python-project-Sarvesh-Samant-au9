import time
import random
import sys
# import winsound
import os
from gtts import gTTS
from googletrans import Translator
# Welcome Message and Explain rules


class Welcome:
    def __init__(self):
        welcomeMessage = """
        -----*****--- Welcome To Snakes And Ladders ---*****-----
        Rules:
        1] A maximum of 4 Players Can participate,
         while a minimum of 2 are necessary to Begin the Game.
        2] Based on Terminal output only no, GUI.(Graphical User InterFace).
        3] You can either decide to Enter the snakes and ladders
         as per your choice or else you can use predefined Board.
        4] Every Player gets Chance one by one.
        5] Two Modes Arcade and Classic are available.
        6] Arcade Mode is in Beta version.
        7] A player reaching 100 would be titled as Winner.
        8] You win You Conquer Best of Luck Players
        9] If you get a 6 you get 1 more extra Chance, if more than
        2 dice faceswould be a 6 then you need not get another chance
         in short at max 1 chance only
        """
        print(welcomeMessage)


# Boards having all 100 Values
# 2 Boards are defined Arcade->
# Userdefined Board(under development), with Validations
# Classic Board is A regular board

class ArcadeBoard:
    def __init__(self):
        msg = """
        1] Here all basic rules are same
        2] You can add all the snakes and ladders as per your choice
        3] Maximum 15 snakes/ladders and minimum of
         2 snakes/ladders can be inserted.
        """
        print(msg)

    snakePos = {}
    laddersPos = {}

    def arcadeMode(self):
        finalSnakes = 0
        finalLadders = 0
        while True:
            numberOfSnakes = int(input("""Enter the Number of
            snakes you want """).strip())

            if numberOfSnakes in range(2, 15):
                finalSnakes = numberOfSnakes
                break
            else:
                print("Maximum of Snakes Can be 14, least would be 4")
                continue
        for i in range(finalSnakes):
            print("""Enter the value of start and
            end for snake {} """.format(i + 1))
            while True:
                insertSnakesStart = abs(int(input("""Enter the Start
                Position """).strip()))
                insertSnakesEnd = abs(int(input("""Enter the End
                Position """).strip()))
                if (insertSnakesStart > insertSnakesEnd) and (
                    insertSnakesStart and insertSnakesEnd < 100) and (
                     insertSnakesStart > 1):
                    ArcadeBoard.snakePos[insertSnakesStart] = insertSnakesEnd
                    break
                else:
                    print("""Snake Start Position
                    need to be higher than Ending position,
                    The board has 100 values, no value can be
                    greater than 100 and greater than 1,
                    For any negative value we convert into positive""")
                    continue

        while True:
            numberOfLadders = int(input("""Enter the Number
            of ladders you want """).strip())

            if numberOfLadders in range(2, 15):
                finalLadders = numberOfLadders
                break
            else:
                print("Maximum of ladder Can be 14, least would be 4")
                continue
        for j in range(finalLadders):
            print("""Enter the value of start and
            end for ladder {} """.format(j + 1))
            while True:
                insertLaddersStart = abs(int(input("""Enter the Start
                 Position for a ladder """).strip()))
                insertLaddersEnd = abs(int(input("""Enter the End
                 Position for a ladder """).strip()))
                if (insertLaddersEnd > insertLaddersStart) and (
                    insertLaddersEnd and insertLaddersStart < 100) and (
                        insertLaddersStart > 1):
                    ArcadeBoard.laddersPos[insertLaddersStart] = insertLaddersEnd
                    break
                else:
                    print("""Ladder Start Position need to be lesser
                     than ending position, The board has 100 values,
                      no value can be greater than 100 and greater than 1,
                    For any negative value we convert into positive""")
                    continue
        print(ArcadeBoard.laddersPos, ArcadeBoard.snakePos)
        return ArcadeBoard.laddersPos, ArcadeBoard.snakePos


class ClassicBoard:
    def __init__(self):
        msg = """
        All Basic Rules nothing New
        """
        print(msg)
    snakes = {}
    ladders = {}

    def classicMode(self):
        ClassicBoard.snakes = {
            32: 10, 36: 6, 48: 26, 62: 18, 88: 24, 95: 56, 70: 44, 99: 23
        }
        ClassicBoard.ladders = {
            2: 30, 4: 14, 8: 10, 28: 74, 50: 67, 71: 92, 88: 99}
        print("""Snakes Will
         be At {} """.format(ClassicBoard.snakes))
        print()
        print("""ladders will
         be at {} """.format(ClassicBoard.ladders))
        return ClassicBoard.snakes, ClassicBoard.ladders
# Press any key to start -concept
# Players and their names are defined


startTheGame = int(input("""Enter a Number to
 start the Game """).strip())
participantsList = []


def playerInfo():
    while True:
        totalPlayers = int(input("Enter the number of Players ").strip())
        if totalPlayers in range(2, 5):
            for i in range(totalPlayers):
                playerId = input("""Enter the Player--{}
                 Name""".format(i + 1)).strip()
                if len(playerId) < 4:
                    playerId = "ply" + playerId
                elif len(playerId) > 15:
                    playerId = playerId[:15]
                else:
                    playerId = playerId
                participantsList.append(playerId)
            break
        else:
            print("Players should be at maximum 4 or minimum of 2 are allowed")
    return participantsList


def get_player_names():
    playerInfo()
    if len(participantsList) == 2:
        print("""Game Between {}
        and {}""".format(participantsList[0], participantsList[1]))
        return participantsList[0], participantsList[1]
    elif len(participantsList) == 3:
        print("""A 3-way competition in
         between {}, {} and
          {}""".format(
          participantsList[0],
          participantsList[1],
          participantsList[2]))
        return participantsList[0], participantsList[1], participantsList[2]
    elif len(participantsList) == 4:
        print("""A Fatal 4 way amongst Fantastic 4 {},
         {}, {} and {}""".format(
         participantsList[0],
         participantsList[1],
         participantsList[2],
         participantsList[3]))
        return (
            participantsList[0], participantsList[1],
            participantsList[2], participantsList[3])

# Small puns to make this more interactive, this are
# triggered in randomized manner using random.choice()
# When Snake comes this puns are triggered


def snakeQuotes():
    snake_bite = [
        "You will be Punished",
        "sssssss I gonna throw you Down Bye!!",
        "I cannot tolerate your intolerance any more",
        "AHHH you destroyed be prepared",
        "I hate python so you will be going Down"
    ]
    return snake_bite


# Puns to alert Player for his/her chance
def playerQuotes():
    player_turn_text = [
        "Lets Move On Buddy",
        "Go.",
        "Please Please Please a six this time",
        "Lets Charge and prepare for Glory",
        "Ready You??  ",
        "",
    ]
    return player_turn_text


# Puns triggered when a ladder appears
def ladderQuotes():
    ladder_jump = [
        "I am here to save you and help you to reach your destiny",
        "Superb ladder takes me to the top Wooooowwww!!",
        "Gottcha man",
        "Success shortcut",
        "Got it Lottery!!!"
    ]
    return ladder_jump


# For dice throw inteded puns
def diceRolls():
    diceQuotes = [
        "Dice is Rolling",
        "Gottacha Dice ",
        "Dice is in air",
        "get the numberr on dice face"
    ]
    return diceQuotes


# Get Dice Value in randomized sense using random.randint()
def diceValue():
    time.sleep(1)
    diceNumber = random.randint(1, 6)
    diceFace = diceNumber
    if diceNumber > 4:
        print("Ahha you got it ", str(diceNumber))
        while diceNumber == 6:
            diceNumber = random.randint(1, 6)
            diceNumber = diceFace + diceNumber
            print("You get another Chance")
            print("For next chance you get {} ".format(diceNumber))
    else:
        print("Its a {}".format(str(diceNumber)))
    return diceNumber

# Printing if snake bites it takes player-name,
# the oldvalue where snake has its head and
# the current value where snake has its tail


def gotSnakeBite(oldValue, currentValue, playerName):
    print(random.choice(snakeQuotes()))
    print("""Snake bites {}, falls from {}
     to {}""".format(playerName, oldValue, currentValue))


# Printing if ladders help it takes player-name,
# the oldvalue where ladder has its lowpoint and the current value
# where ladder has its end or top most point


def got_ladder_jump(oldValue, currentValue, playerName):
    print(random.choice(ladderQuotes()))
    print("""Ladder helps {}, climbs
     from {} to {}""".format(playerName, oldValue, currentValue))


# Main logic and recalls other functions like dice
# value and calculates the space where the palyer will move


# Logic for arcade Mode

def snakesAndLadders(playerName, currentValue, dice_value):
    if getInput == "arcade":
        time.sleep(1)
        oldValue = currentValue
        currentValue = currentValue + dice_value
        print("""{} moved from {} to
         {}""".format(playerName, oldValue, currentValue))

        if currentValue > 100:
            print("""You need {} to win this game.
             Don't loose hope.""".format(100 - oldValue))
            return oldValue

        if currentValue in ArcadeBoard.snakePos:
            finalValue = ArcadeBoard.snakePos.get(currentValue)
            gotSnakeBite(currentValue, finalValue, playerName)

        elif currentValue in ArcadeBoard.laddersPos:
            finalValue = ArcadeBoard.laddersPos.get(currentValue)
            got_ladder_jump(currentValue, finalValue, playerName)

        else:
            finalValue = currentValue

        return finalValue

# Logic for Classic Mode
    elif getInput == "classic":
        time.sleep(1)
        oldValue = currentValue
        currentValue = currentValue + dice_value
        print("""{} moved from
         {} to {}""".format(playerName, oldValue, currentValue))

        if currentValue > 100:
            print("""You need {} to win this game.
             Don't loose hope.""".format(100 - oldValue))
            return oldValue

        if currentValue in ClassicBoard.snakes:
            finalValue = ClassicBoard.snakes.get(currentValue)
            gotSnakeBite(currentValue, finalValue, playerName)

        elif currentValue in ClassicBoard.ladders:
            finalValue = ClassicBoard.ladders.get(currentValue)
            got_ladder_jump(currentValue, finalValue, playerName)

        else:
            finalValue = currentValue

        return finalValue


# to put the end to the game First Player to reach 100 Wins


def check_win(playerName, position):
    time.sleep(1)
    if position == 100:
        print("Thats it. {} won the game.".format(playerName))
        print("Congratulations  {}.".format(playerName))
        print("Thank you for playing the game.")
        print("Rate Us")
        sys.exit(1)

# getting positions of Players


def start():
    time.sleep(1)
    get_player_names()
    time.sleep(1)
    player1_current_position = 0
    player2_current_position = 0
    player3_current_position = 0
    player4_current_position = 0
    while True:
        if len(participantsList) == 2:
            player1 = participantsList[0]
            player2 = participantsList[1]
            time.sleep(1)

            input1 = input(""" {} : {} Hit the enter to
             roll dice: """.format(player1, random.choice(playerQuotes())))
            print(random.choice(diceRolls))
            diceFaceValue = diceValue()
            time.sleep(1)
            print(player1 + " Progressss....")
            player1_current_position = snakesAndLadders(
                player1, player1_current_position, diceFaceValue)
            check_win(player1, player1_current_position)

            input_2 = input(""" {} : {} Hit the enter
             to roll dice: """.format(player2, random.choice(playerQuotes())))
            print(random.choice(diceRolls))
            diceFaceValue = diceValue()
            print(player2 + " Charges.......")
            player2_current_position = snakesAndLadders(
                player2, player2_current_position, diceFaceValue)
            print()
            check_win(player2, player2_current_position)

        elif len(participantsList) == 3:
            player1 = participantsList[0]
            player2 = participantsList[1]
            player3 = participantsList[2]
            time.sleep(1)

            input1 = input(""" {} : {} Hit the enter to roll dice: """.format(
                player1, random.choice(playerQuotes())))
            print(random.choice(diceRolls()))
            diceFaceValue = diceValue()
            time.sleep(1)
            print(player1 + " Progressss....")
            player1_current_position = snakesAndLadders(
                player1, player1_current_position, diceFaceValue)
            check_win(player1, player1_current_position)

            input_2 = input(""" {} : {} Hit the enter to
             roll dice: """.format(player2, random.choice(playerQuotes())))
            print(random.choice(diceRolls()))
            diceFaceValue = diceValue()
            print(player2 + " Charges........")
            player2_current_position = snakesAndLadders(
                player2, player2_current_position, diceFaceValue)
            print()
            check_win(player2, player2_current_position)

            input_3 = input(""" {} : {} Hit the enter
             to roll dice: """.format(player3, random.choice(playerQuotes())))
            print(random.choice(diceRolls()))
            diceFaceValue = diceValue()
            time.sleep(1)
            print(player3 + " Attacks..............")
            player3_current_position = snakesAndLadders(
                player3, player3_current_position, diceFaceValue)
            print()
            check_win(player3, player3_current_position)

        elif len(participantsList) == 4:
            player1 = participantsList[0]
            player2 = participantsList[1]
            player3 = participantsList[2]
            player4 = participantsList[3]
            time.sleep(1)

            input1 = input(""" {} : {} Hit the enter to roll dice: """.format(
                player1, random.choice(playerQuotes())))
            print(random.choice(diceRolls()))
            diceFacevalue = diceValue()
            time.sleep(1)
            print(player1 + " Progressss....")
            player1_current_position = snakesAndLadders(
                player1, player1_current_position, diceFacevalue)
            check_win(player1, player1_current_position)

            input_2 = input("""{} : {} Hit the enter to roll dice: """.format(
                player2, random.choice(playerQuotes())))
            print(random.choice(diceRolls()))
            diceFaceValue = diceValue()
            time.sleep(1)
            print(player2 + " Charges........")
            player2_current_position = snakesAndLadders(
                player2, player2_current_position, diceFacevalue)
            print()
            check_win(player2, player2_current_position)

            input_3 = input(""" {} : {} Hit the enter to roll dice: """.format(
                player3, random.choice(playerQuotes())))
            print(random.choice(diceRolls()))
            diceFacevalue = diceValue()
            time.sleep(1)
            print(player3 + " Attacks.....")
            player3_current_position = snakesAndLadders(
                player3, player3_current_position, diceFacevalue)
            print()
            check_win(player3, player3_current_position)

            input_4 = input(""" {} : {} Hit the enter to roll dice: """.format(
                player4, random.choice(playerQuotes())))
            print(random.choice(diceRolls()))
            diceFaceValue = diceValue()
            time.sleep(1)
            print(player4 + " Hopes........")
            player4_current_position = snakesAndLadders(
                player4, player4_current_position, diceFacevalue)
            print()
            check_win(player4, player4_current_position)

# Driver Code User Based


if __name__ == "__main__":
    inputList = ["arcade", "classic"]
    print(inputList)
    getInput = input("Enter Mode as per your comfort").strip().lower()
    if getInput == inputList[0]:
        arcadeGame = ArcadeBoard()
        arcadeGame.arcadeMode()
    else:
        classicGame = ClassicBoard()
        classicGame.classicMode()
    welcome = Welcome()
    # fileHandling = languagesAttainu.returnLanguages()

    trans = Translator()
    listsLanguage = ["", "English", "Hindi", "Marathi", "Tamil", "kannada"]
    lists = ["", "en", "hi", "mr", "ta", "kn"]
    print(listsLanguage)
    while True:
        inputMyPreferredLanguage = int(input("Select the Language"))
        if inputMyPreferredLanguage in range(1, 6):
            print(listsLanguage[inputMyPreferredLanguage])
            code = lists[inputMyPreferredLanguage]
            break
        else:
            print("Only 5 Languages are available Right now")
            continue
    print(code)

    t = trans.translate(
            """Hi! I am Google Assistant, I will read all the
            instructions before beginning of the Game.Kindly listen!
            Welcome To Snakes And Ladders
            Rules:
            Rule-1. A maximum of 4 Players Can participate,
            while a minimum of 2 are necessary to Begin the Game.
            Rule-2. Based on Terminal output only no,
            Graphical User Interface (GUI).
            Rule-3. You can either decide to Enter the snakes and
            ladders as per your choice or else you can use predefined Board
            Rule-4. Every Player gets Chance one by one.
            Rule-5. Two Modes Arcade and Classic are available.
            Rule-6. Arcade Mode is in Beta version.
            Rule-7. A player reaching 100 would be titled as Winner.
            Rule-8. You win You Conquer Best of Luck Players.
            Rule-9. If you get a 6 you get 1 more extra Chance,if more than 2
            dice faces would be a 6 then you need not get another
            chance in short at maximum 1 chance
            only. Thank YOU""", src = "en", dest = code
        )

    print(f'Destination: {t.dest}')
    print(f'{t.origin} -> {t.text}')
    listsOut = ["textFile.txt", "hindiText.txt", "marathiText.txt",
                "tamil.txt", "kannada.txt"]
    file = listsOut[inputMyPreferredLanguage - 1]

    fh = open(file, "r", encoding="utf8")
    myText = fh.read().replace("\n", " ")
    language = "en"
    output = gTTS(text=myText, lang=language, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")
    start()


# After game has been completed we get a feedback option
# Feedbacks are recorded and ratings are Displayed

    feedBack = [0, 1]
    print("""{} to not give a feedback and {}
     to give a feedback""".format(feedBack[0], feedBack[1]))
    feedBackStores = int(input("Wanna give FeedBack, Enter here ").strip())
    if feedBackStores == 0:
        print("Thank You Again")
    else:
        print("If you like the game Rate us 5!!")
        comments = []
        while True:
            k = int(input("Enter ratings"))
            if k in range(1, 6):
                print(k, "Rate Here")
                print("*" * k)
                break
            else:
                print("Ratings can be A maximum of 5 and minimum of 1")
                print("Kindly ReEnter")
                continue
        print("Any Improvement is Welcomed ")
        a = input("Comments if any ").strip().capitalize()
        comments.append(a)
        print("""You commented {} and
         rated us {} """.format(comments[0], ("*") * k))
        if k < 2:
            print("""Sorry for inconvineince,
             We are trying to make it better.!!""")
            print("Have a goodDay!!")
        else:
            print("Happy To Hear this from You")
