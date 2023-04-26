#1//
def reduce_adjacent_duplicates(lst):
    result = [lst[0]]  
    for i in range(1, len(lst)):
        if lst[i] != result[-1]:  
            result.append(lst[i])
    return result

input_list = [1, 2, 3, 3]
result_list = reduce_adjacent_duplicates(input_list)
print(result_list)


# 2-a //


string = input("Enter a string: ")
length = len(string)
middle_index = length // 2

front_half = string[:middle_index]
back_half = string[middle_index:]
print("Front half:", front_half)
print("Back half:", back_half)


# # 2-b//

a = input("Enter string a: ")
b = input("Enter string b: ")

a_length = len(a)
b_length = len(b)

a_middle_index = (a_length + 1) // 2
b_middle_index = (b_length + 1) // 2

a_front_half = a[:a_middle_index]
a_back_half = a[a_middle_index:]

b_front_half = b[:b_middle_index]
b_back_half = b[b_middle_index:]

result = (a_front_half + b_front_half) + (a_back_half + b_back_half)

print("Result:", result)


#3//
def are_all_numbers_different(seq):

    return len(seq) == len(set(seq))
x=input("Enter list of numbers ")
print(are_all_numbers_different(x)) 


#4//
def bubble_sort(arr):
    length = len(arr)
    for i in range(length):

        for j in range(length - i - 1):
        
            if arr[j] > arr[j + 1]:
              
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# run
arr = [10, 5, 7, 1, 15, 3, 12]
bubble_sort(arr)
print("Sorted array is:", arr)

#5//
import random

def play_game():

    secret_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100. You have 10 tries to guess it!")
    
    guessed_numbers = []
    num_tries = 0
    
    while num_tries < 10:

        guess = input("Guess a number: ")
        if not guess.isdigit():
            print("That's not a number.")
            continue
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("This number is not allowed.")
            continue
        if guess in guessed_numbers:
            print("You already entered this number before.")
            continue
    
        num_tries += 1
        guessed_numbers.append(guess)
     
        if guess == secret_number:
            print("Congratulations! You guessed the number in", num_tries, "tries.")
            play_again()
            return
        elif guess < secret_number:
            print("Your guess is smaller than i think.")
        else:
            print("Your guess is higher than i think.")
  
    print("Sorry, you ran out of tries. My number was", secret_number)
    play_again()

def play_again():
   
    play_again = input("Do you want to play again? (y/n)")
    if play_again.lower() == "y":
        play_game()
    else:
        print("Thanks for playing!")
play_game()
