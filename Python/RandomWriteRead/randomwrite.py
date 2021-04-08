#Write a series of random numbers to randomnum.txt based on user input

import random

def int_convert(given_num):
    #Convert the number to an interger and check for errors
    try:
        int(given_num)
        if pos_check(given_num):
            return(given_num)
        else:
            return False
    except ValueError:
        print("Please input a valid number.")
        return False
    
def pos_check(given_num):
    #Check to make sure that the number is positive

    if int(given_num) > 0:
        return True
    else:
        return False
    
def user_input():
    #Recieve user input and make sure it fits criteria

    #Get the number of numbers
    while True:
        num_of_num = int_convert(input("Please input the number of numbers to be generated. "))
        if num_of_num == False:
            continue
        else:
            break
    #Get the upper bound
    while True:
        upper_bound = int_convert(input("Please input the upper bound for the numbers. "))
        if upper_bound == False:
            continue
        else:
            break
    #Get the lower bound
    while True:
        lower_bound = int_convert(input("Please input the lower bound for the numbers. "))
        if lower_bound == False:
            continue
        elif int(lower_bound) > int(upper_bound):
            print("The lower bound cannot be greater than the upper bound.")
            continue
        else:
            break

    return(int(num_of_num), int(upper_bound), int(lower_bound))

def write_random(num_of_num, upper_bound, lower_bound):
    #Generate the random numbers and write them to the file

    #Open/create file
    file = open('randomnum.txt', 'w')

    #Generate and write the numbers
    for i in range(num_of_num):
        file.write(str(random.randint(lower_bound, upper_bound)) + '\n')

    #Give confirmation to the user
    file.close()
    print("The numbers have been written to randomnum.txt.")

def main():
    #Perform the main body of the program

    #Activate the functions
    num_of_num, upper_bound, lower_bound = user_input()
    write_random(num_of_num, upper_bound, lower_bound)
    input()
main()
