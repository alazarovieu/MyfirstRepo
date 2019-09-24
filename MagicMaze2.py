password="SSNWES"
fixed="SSNWES"
lives=3
moves=1
counter=0
length=0
reps=0

while True:
    print()
    print("The valid commands are: N,S,E,W or exit.")
    command = input("Please introduce your command: ")

    if command=="EXIT":
        print("Bye!")
        break

    elif command == password:
        print("You won!!!")
        print("You completed the maze in ", str(moves), "moves and ", str(lives), "lives")
        break

    elif len(command)==len(password) and command!=password:
        print("Try again from the beginning.")
        moves+=1
        counter+=1

    elif lives==0:
        print("You are dead. Sorry. Bye!")
        break

    elif len(command)!=len(password):
        length=len(command)
        for i in command:
            reps+=1
            for j in password:

                if i==j and reps==length:
                    print("You are right but try again from the beginning")
                    password = fixed
                    reps = 0
                    moves+=1
                    counter+=1
                    break
                elif i==j:
                    password = password[1:]
                    break

                else:
                    print()
                    print("Sorry, you deviated from the maze's exit.")
                    print("Try again from the beginning.")
                    password = fixed
                    reps=0
                    if counter == 10 or counter == 20 or counter == 30:
                        lives -= 1
                        break
                    break
                    