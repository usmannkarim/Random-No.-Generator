import random
randomnumber=random.randint(1,100)
guesses=0
userguess=None
while(randomnumber != userguess):
    guesses +=1
    userguess=int(input("enter your guess:"))
    if(userguess==randomnumber):
        print("you guessed it right!")
    else:
        if(userguess>randomnumber):
            print("you guessed it wrong!, enter a smaller number")
        else:
            print("you guessed it wrong!, enter a larger number")
print(f"the guessed the number in {guesses} guesses")
with open('hiscorepro.txt','r')as f:
    hiscorepro=int(f.read())
if(guesses>hiscorepro):
    print("you have broken the hiscore")
with open('hiscorepro.txt','w')as f:
    f.write(str(guesses))



