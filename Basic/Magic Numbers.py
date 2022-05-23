import random

magic_numbers = [ random.randint(0,9) , random.randint(0,9)]
answer = " "

#answer = answer.join(magic_numbers)


def ask_user_and_check_number():
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        return "YAY! You got it!"
    if user_number not in magic_numbers:
        return "BOO! You didn't get it!"

def run_program_x_times(chances):
    for attempt in range(chances):
        print("This is attempt {number}".format(number = attempt + 1))
        msg = ask_user_and_check_number()
        print(msg)
    
    print("These were the numbers: {numbers}".format(numbers = " ".join(map(str, magic_numbers))))

tries = int(input("How many tries would you like? (1-10) "))

run_program_x_times(tries)