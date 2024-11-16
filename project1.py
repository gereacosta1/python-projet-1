#Typecasting

name = "gere"
age = 99
gpa = 3.1
is_student = True

name = bool(name)#true
print(name)#si dejara vacio el str name me daria falso


gpa = int(gpa)

print(gpa)

print(type(age))   






#input, conditional and lower()

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




#more inputs things

name = input("what's your name?: ")
age = input("How old are you?: ")

age = int(age)#we need to convert it from str to int before + 1
age = age + 1

print(f"Your name is {name}!, Hello {name}")#we use F first because we use a variable {name}
print("Happy Birthday!!!!")#is not necessary use F becausa we don't use a variable
print(f"Your age is {age}YO!!!")#we use F first because we use a variable {age}

