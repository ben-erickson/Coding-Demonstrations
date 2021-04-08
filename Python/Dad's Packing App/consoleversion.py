#Console Version of dad's packing app
#This version is a minimum viable product, and a proof of concept
#The current numbers are based on assumptions, and not dad's requests

#The user will input the kinds of days that will be on their business trip
#The program will output the clothes that they will need to
#pack in a readable format

def days_input():
    #Recieve user input for what days will be on trip and return values in list

    while True:
        try:
            formal_days = int(input('How many formal days will be on this trip? '))
            break
        except ValueError:
            print('Please only input valid numbers.')
    while True:
        try:
            bc_days = int(input('How many business casual days will be on this trip? '))
            break
        except ValueError:
            print('Please only input valid numbers.')
    while True:
        try:
            cas_days = int(input('How many casual days will be on this trip? '))
            break
        except ValueError:
            print('Please only input valid numbers.')

    #Organize the values into a list and return it

    total_days = formal_days + bc_days + cas_days
    days_list = [total_days, formal_days, bc_days, cas_days]

    return days_list

def clothes_calculate(days_list):
    #Take a list of all the days, figure out what clothes are needed, and return that in a list
    try:
        socks = days_list[0] * 2
        underwear = days_list[0]

        if days_list[3] >= 1:
            cas_shoe = 1
        else:
            cas_shoe = 0

        if days_list[1] >= 1 or days_list[2] >= 1:
            dress_shoe = 1
        else:
            dress_shoe = 0

        suits = days_list[1]
        bc_pants = days_list[2]
        bc_shirts = days_list[2]

        cas_shirts = days_list[3]
        cas_pants = days_list[3]

        clothes_list = [socks, underwear, cas_shoe, dress_shoe, suits, bc_pants, bc_shirts, cas_shirts, cas_pants]
        return clothes_list
    
    except:
        return False

def main():
    #Perform the main functionality of the program
    days_list = days_input()
    packing_list = clothes_calculate(days_list)

    if packing_list == False:
        print('An error occured calculating the packing list. Please restart the app and try again.')
    else:
        print('Individual socks:', packing_list[0])
        print('Underwear:', packing_list[1])
        print('Casual Shoes:', packing_list[2])
        print('Dress Shoes:', packing_list[3])
        print('Suits:', packing_list[4])
        print('Business Casual Shirts:', packing_list[5])
        print('Business Calual Pants:', packing_list[6])
        print('Casual Pants:', packing_list[7])
        print('Casual Shirts:', packing_list[8])


main()

#This is a pretty ugly version of the program, but it should work for now.
#I'd like to make the calculation more streamlined, and based on variables, not hard coded
#There is also the gui, and being to change the values to customize the program





            
