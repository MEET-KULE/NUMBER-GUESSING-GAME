import random
n = random.randint(1,100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Guess the number from 1 to 100 : "))
    if(a > n):
        print("Lower number please !")
        guesses += 1
    elif(a < n):
        print("Higher number please ")
        guesses += 1


print(f"You have guessed the number correctly.The number is {n} and the number of guesses you took is {guesses}")
