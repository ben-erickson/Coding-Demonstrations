#Paint job estimate. Take inputs and return the outputs perscribed by the challenge

#Needed for the .ceil() function
import math

def pos_float(user_input):
    #Take the user input, make sure it is positive, convert to float
    
    while True:
        try:
            final_float = float(user_input)
        except ValueError:
            user_input = input("Please input a decimal number. ")
            continue

        if final_float > 0:
            break
        else:
            user_input = input("Please input a positive number. ")
            continue
        
    return final_float

def main():
    #Perform the main body of the function

    #Obtain the user input
    sq_ft = pos_float(input("Please input the square feet needed to be painted today. "))
    paint_pr = pos_float(input("Please input the price of the paint to be used today. "))

    #Calculate the outputs

    #Gallons
    gallons = math.ceil(sq_ft / 350)

    #Labor
    hrs_labor = round(((sq_ft / 350) * 6),1)
    labor_cost = round((62.25 * hrs_labor),2)

    #Paint Cost
    paint_cost = round((gallons * paint_pr),2)

    #Total Cost
    total_cost = round((paint_cost + labor_cost),2)

    #Output
    print("This job will take " + str(gallons) + " gallons of paint, costing $" + str(paint_cost) + ".")
    print("It will take " + str(hrs_labor) + " hours of labor, costing $" + str(labor_cost) + ".")
    print("Leading to a total cost of $" + str(total_cost) + ".")

while True:
    main()
    end_choice = input("If you would like to complete another estimate, input 'y'. Input 'n' to exit the program. ")
    if end_choice == 'y':
        pass
    else:
        break
