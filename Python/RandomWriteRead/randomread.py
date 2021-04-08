#Read the numbers from randomnum.txt and output some information

def main():
    #Perform the main body of the function

    #Open the file and catch the error
    try:
        num_file = open('randomnum.txt', 'r')

        #Begin reading and outputting the numbers in the file
        print("List of random numbers in randomnum.txt:")

        #Declare a variable to keep count of the amount of numbers
        line_count = 0
        
        #Print the numbers
        for line in num_file:
            line.rstrip('\n')
            print(line)
            line_count += 1

        #Print the number count
        print('Random number count:', line_count)

        input()
        
    except IOError:
        print("The file does not exist. Run randomwrite.py to generate some random numbers.")

main()
