from argparse import ArgumentDefaultsHelpFormatter
import re
import random


points = 0
used_words = []
fouls = []
result = None


if points < 0:
    points = 0


def search(lastLetter):
    global mechanicalFailure
    global used_words
    file_handle = open("readme.md")
    words_list2 = []
    for line in file_handle:
        line.rstrip()
        words = re.findall(f"^({lastLetter}.+)", line)
        for item in words:
                if item not in used_words:
                    words_list2.append(item)
    if len(words_list2)== 0:
        mechanicalFailure()
    return words_list2
                


def analysis():
    print(points)
    g = input("Enter 'y' if you want to know the fouls and 'n' if not:\n")
    if g == 'y':
        if len(fouls) > 0:
            i = 1
            for foul in fouls:
                print(f"Foul.{i} : {foul}")
                i += 1
        else:
            print("You haven't done any fouls..")
    elif g == 'n':
        pass
    else:
        print("Something went wrong, try again..")
    print("Thanks for playing this game")
    


def mechanicalFailure():
    print("Computer doesn't have any word")
    print("Computer aborted\nHence you won")
    analysis()
    


def findLastLetter(word):
    word = str(word)
    lastLetter = word[len(word) - 1]
    return lastLetter
    


def syllable_loop():
    global used_words
    global points
    userInput = ""
    userInput_2 = ""
    while userInput != "abort":
        userInput = input("Type your word, or type 'abort' if you don't have any word, or type '@' for rules : \n")
        used_words.append(userInput)
        if userInput_2 == "abort" or userInput == "abort":
            print("Game Over...")
            print("You lost the game, you're a noob")
            break
        if userInput == "@":
            with open("rules.md") as u:
                for lines in u:
                    print(lines, end="\n")
            continue
        if userInput.isnumeric():
            points -= 1
            fouls.append("Entered integer instead of words")
            print("Sorry, try again.....")
            print("You can't choose any number\n")
            continue
        if userInput.isalpha():
            global findLastLetter
            lastLetter = findLastLetter(userInput)
            words_list = search(lastLetter)
            bts = []
            for i in words_list:
                bts.append(i)
            display_word = random.choice(bts)
            print(f"The last letter of {userInput} is {lastLetter}. And here is the word\n{display_word}\n")
                            
            while userInput_2 != "abort":
                lastLetter_2 = findLastLetter(display_word)
                userInput_2 = input(f"Type a word starting from {lastLetter_2} (type 'abort' if you don't have any word):\n")
                if userInput_2 in used_words:
                    points -= 1
                    fouls.append("You duplicated the word which was previously used")
                    print(points)
                    print(f"{userInput_2} is already used, you can't take it again")
                    print("Try again..")
                    continue
                if userInput_2.isnumeric():
                    fouls.append("Entered integer instead of words")
                    points -= 1
                    print(points)
                    print("Sorry, try again.....")
                    print("You can't choose any number")
                    continue
                elif userInput_2.isalpha() and userInput_2 != "abort":
                    used_words.append(userInput_2)
                    if lastLetter_2 == userInput_2[0]:
                        words_list = search(findLastLetter(userInput_2))
                        display_word = random.choice(words_list)
                        print(f"The last letter of {userInput_2} is {findLastLetter(userInput_2)}. And here is the word\n{display_word}")
                        used_words.append(display_word)
                        points += 1
                        print(points)
                    else:
                        fouls.append("You violated the basic rule by not entering the appropriate word")
                        print(points)
                        points -= 1
                        continue
                else:
                    print(points)
                    points -= 1
                    fouls.append("You entered non-allowed invalid characters")
                    print("Sorry, try again..")
                    print("These character aren't allowed")
                    continue
                continue
            result = "You lost\nYou are a noob.."
            print(result)
            break
        else:
            print(points)
            fouls.append("You entered non-allowed invalid characters")
            points -= 1
            print("Sorry, try again....")
            print("These characters aren't allowed")
                       
                        
                        
        
            

if __name__ == '__main__':
    syllable_loop()
    analysis()
    

    
    
   

