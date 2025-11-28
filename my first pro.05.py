import random
while True:
 mainumber = random.randint(0,20)
 print('I am thinking of a number between 1 and 20')
 for i in range(1,7):
    print('Take a guess')
    guess = int(input())

    if guess<mainumber:
        print('you are too low')
    elif guess>mainumber:
        print('you are too high')
    else:
        break

 if guess == mainumber:
    print('Good job! You guessed my number in ' + str(i) + ' guesses!')
 print('DO you want to play again')
 againplay = input()
 if againplay == "yes":
    print ('wea;com')
    continue
 else:
    print('sorry,You guess number:'+str(i)+ 'incarect try agean.')


