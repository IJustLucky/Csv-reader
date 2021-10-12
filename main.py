import csv

arr = []
int_array = []
with open('D:/cities.csv', mode='r') as file:
    csvFile = csv.reader(file)
    csvFile = list(csvFile)

# print(arr)

# int(arr[0])
# sum(arr[0])

# Take first 3 elements in lines and put in array(excluding first line- first line does not have numbers)
for lines in csvFile:
    arr.append(lines[0:3])
arr = arr[1:]
print(arr)


# Convert the array of arrays to single arrays

# Take each array and covert values to int in a new array

def intconverter(stringed_array):
    stringed_array = ["1", "2", "4"]
    """This function modifies the array to convert strings to an int"""
    for string in stringed_array:
        while stringed_array[0:] < len(stringed_array):
            string = int(string)
            int_array.append(string)
            break
        print(type(string), string)
        print(int_array)


for degrees_of_lat in arr:
    intconverter(degrees_of_lat)

# Take the 3 elements and convert them into a int from str


# Sum the total of the ints and print them for each line
