import random
#Create an animal class

class AnimalClass:
    #Class to represent different animals

    def __init__(self, animal_type, name):
        #Establish animal attributes

        self._animal_type = animal_type
        self._name = name

        #Establish mood with a random number and assign the proper string
        mood = random.randint(1,3)
        if mood == 1:
            self._mood = 'happy'
        elif mood == 2:
            self._mood = 'hungry'
        else:
            self._mood = 'sleepy'

    def get_animal_type(self):
        #Return animal type
        return self._animal_type

    def get_name(self):
        #Return name
        return self._name

    def check_mood(self):
        #Return mood
        return self._mood
