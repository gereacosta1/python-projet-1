name = input("hey type your name: ")
print("hello "+name+ " welcome to my game!")

should_we_play = input("do you want to play? ").lower()

if should_we_play == "yes" or "y":
        print("we are gonna play!!")
        #weapon = input("choice a weapon (sword/axe): ").lowe()

        direction = input("do you want to go to the left or right? (left/right)").lower()
        if direction == "left":
            print("bad idea, we fell of a cliff, game over!!")
        elif direction == "right":
            choice = input("okey, you know see a bridge, do you want to swim under it or cross it? (swim/cross) ")
            if choice == "swim": #and weapon == "axe" 
                print("you got eaten by alligator, you die, the end")
            else:
                print("you won,  ")
        else:
            print("try a valid opcion or u die")

else:
        print("we are NOT playing...")