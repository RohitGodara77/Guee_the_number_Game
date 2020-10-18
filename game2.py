import random
n = random.randint(1,100)

g = int(input("you thing you are smart, guess the number?? "))

t = 0
f = True

while(f):
    if g == n:
        f = False
        print(f'Good! correct guess,you made {t} guesses to make the correct one')
    elif g > n:
        t+=1
        print('guess a smaller number : ')
        g = int(input())
    else:
        t+=1
        print('guess a larger number :')
        g = int(input())