numbers = [1,2,3,4,5,6,7,9,10]

while True:
    guess = input("Guess a number or type q to quit. ")
    if guess == 'q':
        break
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a number.")
    if guess in numbers:
        print("Yes that number is in the list!")
    else:
        print("NO! Try again!")
