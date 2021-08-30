# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
sol = []
def countdown(x):
    for i in range(x, -1, -1):
        sol.append(i)
countdown(11)
print(sol)
# Example: countdown(5) should return [5,4,3,2,1,0]




# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def pandr(first,second):
    print(first)
    return second
myList = [3, 7]
print(pandr(myList[0], myList[1]))
# Example: print_and_return([1,2]) should print 1 and return 2



# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
myList = [1,2,3,4,5]
def firstPlusLength(x):
    sum = x[0] + len(x)
    return sum
print(firstPlusLength(myList))
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)



# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
myList = [5,2,3,2,1,4]
myListSecond = [3]
def valGreater(x):
    new = []
    for i in range(0,len(x)):
        if len(x) < 2:
            return False
        elif x[i] > x[1]:
            new.append(x[i])
    print(len(new))
    return new

print(valGreater(myList))
print(valGreater(myListSecond))
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False



# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def thisLength(size,value):
    myLengthList = []
    for i in range(0,size):
        myLengthList.append(value)
    return myLengthList
print(thisLength(4,7))
print(thisLength(6,2))
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]