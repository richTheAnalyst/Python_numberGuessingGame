import random

low = 1
high = 100
answer = random.randint(low, high)

print(answer)
guesses =[]
is_running = True

print("Python number guessing game ")
print(f"Select a number between {low} and {high} \n")

while is_running:
    guess = input("Enter your number: \n")

    if guess.isdigit():
        guess = int(guess)
        guesses.append(guess)
        if guess  > high or guess < low :
            print(f"{guess} is out of range")
            print("Please Select a number between {low} and {high}")
        elif guess > answer:
            print("This number is greater than the answer....try again!.")
        elif guess < answer:
             print("This number is lesser than the answer....try again!.")
        if guess == answer:
            print("That is the answer!!!.")
            is_running = False
    else:
        print("Invalid guess")
        print(guesses, end=" ")
        is_running = False


        






        
 



        
       


