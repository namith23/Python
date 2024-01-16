print('Welcome to Treasure Island.Your mission is to find the treasure')
choice1 = input('you are at a crossroad where do u want to go?"left" or "right"').lower()

if choice1 == "left":
    choice2 = input('Do you want to "swim" or "wait" ').lower()
    if choice2 == "wait":
        choice3 = input('Which color door do u choose? "Red","Yellow","Blue"').lower()
        if choice3 == "red":
            print('Burned by fire.Game Over.')
        elif choice3 == "yellow":
            print('You win')
        elif choice3 == "blue":
            print('Eaten by beasts.Game Over.')
        else:
            print('Game over')
        
    else:
        print('Attacked by trout.Game Over.')    
else:
    print('Fall into a hole.Game Over')
   