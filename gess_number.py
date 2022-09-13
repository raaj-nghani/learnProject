# n = 10
# guess = 5
# while (guess <=5):
#     num = int(input("Guess the numner: "))
#     if num < n:
#         print("you entered small number enter big number")
#     elif num > n:
#         print("you entered bigger number enter small number")
#     else:
#         print("you won")
#         print("you take ", guess)
#         break
#     print("guesses is left",guess = guess -1 )
# if(guess>9):
#     print("game over")
#
#
#
n=10
number_of_guess = 1
print("number of guess is 9")
while(number_of_guess<=9):
    guess_number = int(input("Guess the numner \n"))
    if guess_number<n:
        print("small number enter bigger number")
    elif guess_number>n:
        print("big number enter smaller number")
    else:
        print("you won \n")
        print("you took ", number_of_guess)
        break
    print("no of guesses left", 9-number_of_guess)
    number_of_guess = number_of_guess +1
if number_of_guess>9:
    print("game ove")