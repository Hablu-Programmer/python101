word = "Hablu"

Chances = 5
GuessAdd = []
done = False

while not done:
    for letter in word:
        if letter.lower() in GuessAdd:
            print(letter, end = " ")
        else:
            print("_", end = " ")


    MyGuess = input(f"text here {Chances}, next guess: ")
    GuessAdd.append(MyGuess.lower())
    if MyGuess.lower() not in word.lower():
        Chances -= 1
        if Chances == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in GuessAdd:
            done= False

if done:
    print(f"you found the word {word}")
else:
    print(f"game over, The Word Is {word}")