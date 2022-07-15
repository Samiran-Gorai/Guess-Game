import random
jackpot=random.randint(1,100)
guess=int(input("Guess the Number Between 1 and 100 : "))
counter=1
while guess!=jackpot:
    if guess>jackpot:
        print("Wrong Answer, Guess lower number")
    else:
        print("Wrong Answer, Guess higher number")
    guess=int(input("Guess again : "))
    counter+=1
print("Corect Answer. Your Point : ",counter) 
