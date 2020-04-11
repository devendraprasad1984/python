ver = '0.1'


def printTest():
    print("Testing of my first python!!")
    a = 10
    b = 20
    c = a + b
    print("The sum of " + str(a) + " & " + str(b) + " is " + str(c))
    print("The sum is", c)
    print("The sum of", a, "&", b, "is", c)
    # name=input("Whats your name: ")
    # print("The input name was \""+name+"\"")

    number = 23
    # guess = int(input('Enter an integer : '))
    guess = 10
    if guess == number:
        print('Congratulations, you guessed it.')
        print('(but you do not win any prizes!)')
    elif guess < number:
        print('No, it is a little higher than that')
    else:
        print('No, it is a little lower than that')
    print('Done')
    if guess == number:
        print('Congratulations, you guessed it.')
        print('(but you do not win any prizes!)')
    elif guess < number:
        print('No, it is a little higher than that')
    else:
        print('No, it is a little lower than that')
    print('Done')
    # end function

    # printTest()
