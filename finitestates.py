state = 1
while (1):
    userInput = input('Enter you input : ')
    print('You have pressed: ', userInput)

    if state == 1:
        if userInput == 'A':
            state = 2
    elif state == 2:
        if userInput == 'W':
            state = 3
        elif userInput == 'S':
            state = 1
    elif state == 3:
        if userInput == 'D':
            state = 1
    print('Right now you are in state: ', state)
