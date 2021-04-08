#Read numbers from a file and display information about those numbers

#Declare variables for later
file_name = 'numbers.txt'
max_num = 0
min_num = 0
num_count = 0
num_sum = 0
num_average = 0
num_range = 0

try:
    num_file = open(file_name, 'r')

    for line in num_file:
        num_sum += int(line)
        num_count += 1

        if num_count == 1:
            min_num = int(line)

        if int(line) > max_num:
            max_num = int(line)
        elif int(line) < min_num:
            min_num = int(line)

    num_file.close()

    #Calculate the remaining numbers
    num_average = num_sum / num_count
    num_range = max_num - min_num

    print("File name: " + file_name)
    print("Sum: " + str(num_sum))
    print("Count: " + str(num_count))
    print("Average: " + str(num_average))
    print("Maximum: " + str(max_num))
    print("Minimum: " + str(min_num))
    print("Range: " + str(num_range))

    input()
except:
    print("An error occured reading the file.")


