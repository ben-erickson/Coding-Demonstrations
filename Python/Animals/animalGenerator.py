#This program will create a class from Animal.py based on user input
import Animal

def animal_create():
    #Take user input and create an instance of the animal class
    
    name = input("What is the animal's name? ")
    animal_type = input("What kind of animal would you like to make? ")

    new_animal = Animal.AnimalClass(name,animal_type)

    return new_animal

def animal_output(animal_list):
    #Format and output the information using the Animal methods

    try:
        for list_animal in animal_list:
            name = list_animal.get_name()
            animal_type = list_animal.get_animal_type()
            mood = list_animal.check_mood()

            print(name.capitalize(), 'the', animal_type.capitalize(), 'is', mood)
    except ValueError:
        print('This function only accepts lists. Sorry.')
        
def user_interface():
    #Function to allow the user to use the program

    #Declare animal_list as an empty list
    animal_list = []

    #Loop to create new instances of Animal
    while True:
        var_animal = animal_create()
        animal_list.append(var_animal)

        user_continue = input("Would you like to create another animal? (y/n) ")

        if user_continue == 'y':
            continue
        else:
            animal_output(animal_list)
            input()
            break

user_interface()
    
