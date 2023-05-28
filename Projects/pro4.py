answer  = input("Do You Want To Play This Advanture Game? [Yes/No] ")

if answer == "yes":
    print("welcome buddy ")
    answer = input("do you want to explore the cave / jungle [cave/jungle]" )
    if answer == "cave":
       print("you go into the cave and see bear sleeping ")

       answer = input("do you want to fight or run? [fight/run]")
       if answer == "fight":
           print("bears are really strong! you lose")
       elif answer == "run":
           print("you run away! you won")
       else:
           print("oh! you loss man!")
    elif answer == "jungle":
        print("you meet a tiger & You Eateen")
    else:
        print("invilied options!")
else :

    print("play this game if you want to enjoy your self!")
