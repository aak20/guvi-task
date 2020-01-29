import random
chance=5
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print("WELCOME")
a=random.choice(num)
print("guess a number between 1-20")
while chance!=0:
    b=int(input("ENTER YOUR NUMBER :"))
    if b==a:
        print("you won!!!!")
        break
    else:
        print("TRY AGAIN")
    chance=chance-1
print("GAME OVER!!! the correct answer is",a)
