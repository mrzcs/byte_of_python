number = 23
running = True

while running:

    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congras, you guessed it.')
        running = False
    elif guess < number:
        print('NO, it is a little higher than that')
    else:
        print('No, it is a little lower than that')
else: # you can have an else clause for the while loop
    print('The while loop is over.')

print('Done')