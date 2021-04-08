#Recieve input from the user and perform the given equation on the data

def main():
    init_pos = float(input('Please input the initial position of the object. '))
    init_vel = float(input('Please input the initial velocity of the object. '))
    acc = float(input('Please input the acceleration of the object. '))
    time = float(input('Please input the time passed. '))

    final_pos = init_pos + init_vel*time + (.5*acc*(time**2))

    return final_pos

print(main())
