print('whatup!')

L1 = ["john", 102, "USA"]
print(type(L1))

tup = ("apple", "mango", "banana", "orange")
print(type(tup))
print(tup)
# tup[2] = "papaya"

employee = {"Name": "John", "Age": 30, "Salary": 250000, "Company": "GOOGLE"}
print(type(employee))
print("Printing employee data......")
print(employee)

# Printing prime number 
# Method - 1
min = int(input("Enter the min: "))
max = int(input("Enter the max: "))
for n in range(min, max + 1):
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                break
        else:
            print(n,end=" ")

# Method - 2
numr = int(input("Enter range: "))
print("Prime numbers:",end=" ")
for n in range(1, numr+1):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n,end=" ")

# Sorting elements in the list
# Method - 1
mylist = [5, 8, 9, 6, 3]

for i in range(len(mylist)):
    for j in range(i+1, len(mylist)):
        if mylist[j] > mylist[i]:
            mylist[i], mylist[j] = mylist[j], mylist[i]
print(mylist)

# Method - 2
mylist = [2, 5, 7, 5, 3, 4, 5, 2]
asc = []
while mylist:
    min = mylist[0]
    for i in mylist:
        if i < min:
            min = i
    asc.append(min)
    mylist.remove(min)
print(asc)

# Find maximum number from an array
arr = [15, 4, 3, 6, 9]
max = arr[0]
for i in arr:
    if i > max:
        max = i
print(max)

# For asending
mylist = [5, 8, 9, 6, 3]
new = sorted(mylist)
print(new)

# For descending
mylist = [5, 8, 9, 6, 3]
new = sorted(mylist, reverse=True)
print(new)

# Find duplicate value and sort in descending order
mylist = [2, 5, 7, 5, 3, 4, 5, 2]

def duplicate(mylist):
    empty = []
    asc = []

    for i in mylist:
        if i not in empty:
            empty.append(i)
    
    while empty:
        min = empty[0]
        for i in empty:
            if i < min:
                min = i
        asc.append(min)
        empty.remove(min)
    return asc  

ans = duplicate ([2, 5, 7, 5, 3, 4, 5, 2])
print('Duplicate values are:',ans)

# to find substring using diffrent functionalities 
str = 'hello hello whatup hello'
count = str.count('hello')
print(count)
find = str.find('hello')
print(find)
index = str.index('hello') # same as find but returns ValueError if string not present
print(index)
end = str.endswith('o')
print(end)
start = str.startswith('h')
print(start)

# Program to find the factorial of a number
num = int(input("Enter the num: "))
fact = 1

for i in range(1, num+1):
    fact = fact * i
print(f'The factorial of {num} is {fact}')

# Find maximum number from an array
arr = [5, 4, 3, 6, 9]
max = arr[0]
for i in arr:
    if i > max:
        max = i
print(max)

# sorting list in ascending order
mylist = [5, 8, 6, 3, 9]
empty = []
while mylist:
    min = mylist[0]
    for i in mylist:
        if i < min:
            min = i
    empty.append(min)
    mylist.remove(min)
print(empty)

# Python program to find second largest number in a list
list1 = [10, 20, 20, 2, 4, 45, 54, 34, 15]
# Removing duplicates from the list
list2 = list(set(list1))
list2.sort()
print("Second largest element is:", list2[-2])

# Fibonacci series (while loop)
n = int(input("Enter range: "))
f1=0
f2=1
c=2
print(f1, f2, end=", ")
while c<n:
    f = f1+f2
    print(f)
    f1, f2 = f2, f
    c+=1


# Program to generate Fibonacci series [list based iteration]
def fibonacci(n):
    a, b = 0, 1
    fib = [a, b]

    for i in range(2, n):
        c = a+b
        fib.append(c)
        a, b = b, c
    return fib

n = int(input("Enter the range: "))
print(fibonacci(n))


# Use of array
import array
from array import *

# Create an array 'a' of type 'i' (signed integer) with specified elements
a = array('i', [5, 6, -7, 8])

# Create an array 'b' of type 'u' (Unicode character) with specified elements
b = array('u', ['a', 'e', 'i', 'o', 'u'])

# Print the elements of array 'a'
print("The array elements are:")
for element in a:
    print(element)

# Print the elements of array 'b'
for ch in b:
    print(ch)



# Program perfrom operations on another array using an existing array 
from array import *

# Create an array arr1 of type 'd' (double) with specified elements
arr1 = array('d', [1.5, 2.5, -3.5, 4])

# Print the elements of arr1 using a for loop
print('The arr1 elements are:')
for j in arr1:
    print(j, end=' ')

# Create a new array arr2 using a generator expression
arr2 = array(arr1.typecode, (a * 3 for a in arr1))

# Print the elements of arr2 using a for loop
print('\nThe arr2 elements are:')
for i in arr2:
    print(i, end=' ')



# Program to calculate the length of an array using len() with two separate loops 
from array import *
x = array('i', [10, 20, 30, 40, 50])
n = len(x)
print(f"Length of the array is {n}")

# Using a for loop
print("Using for loop")
for i in range(n):
    print(x[i], end=" ")

# Using a while loop
print("\nUsing while loop")
j = 0
while j < n:
    print(x[j], end=" ")
    j += 1


''' Program to print the following pattern 
* 
* * 
* * * 
* * * * 
* * * * * * '''

for i in range(1, 6):
    for j in range(1, i+1):
        # print('* '*(i))    # another way to print 
        print('* ', end='')  # Print a single asterisk with a space, without moving to the next line
    print()  # Move to the next line after each inner loop iteration



# Program to print the right triangle
n = 50  # Initial spacing

for i in range(1, 11):  # Loop from 1 to 10
    # Print spaces for formatting
    print(' ' * n, end="")

    # Print stars in the first half of the row
    print('* ' * (i))

    # Print spaces for formatting in the second half
    print(' ' * (n - i) + '* ' * (i))

    # Decrease the spacing
    n -= 1



# Program to reverse the digits of a number
a = int(input("Enter the number: "))
r = 0
while a!=0:
    r = r*10 + a%10
    a = a//10
print(r)

# Program to differentiate odd and even numbers and sort them 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def sort_numbers(numbers):
    even_numbers = []
    odd_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return (even_numbers, odd_numbers)
even_numbers, odd_numbers = sort_numbers(numbers)
print(even_numbers)
print(odd_numbers)

# Same program by using list comprehension method
def sort_numbers(numbers): # type: ignore
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return (even_numbers, odd_numbers)

# Using lambda function
def sort_numbers(numbers):
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
    return (even_numbers, odd_numbers)


# Program to print the duplicate elements in a list 
my_list = [1, 2, 3, 2, 4, 3, 5, 6, 7, 5, 8, 9, 9]

# Create an empty list to store duplicate elements
duplicates = []

# Create a set to store unique elements
seen = set()

# Iterate through each element in the list
for num in my_list:
    # If we have already seen this element, it is a duplicate
    if num in seen:
        duplicates.append(num)
    else:
        seen.add(num)
print(duplicates)


# Program for lists to store marks, calculate their sum and percentage.
str = input('Enter marks: ').split(' ')
str = (50, 56, 75, 67, 45)
marks = [int(num) for num in str]
sum = 0
for x in marks: 
    print(x)
    sum += x
print(f'Total marks: {sum}')

n = len(marks)
percent = sum / n
print(f'Percentage: {percent}%')


# Program to count the number of occurrences in an array
from array import *

arr = array('i', [1, 2, 3, 4, 2, 4, 5, 1, 6, 2, 6])
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
    
for num, count in freq.items():
    print(f"NUM: {num} | COUNT: {count} ")


# Program of Bubble Sort algorithm to sort the array in ascending order.
from array import *

# Create an empty array to store integers
x = array('i', [])

# Store elements into the array x
n = int(input('No. of elements: '))
for i in range(n):
    x.append(int(input(f'Enter element {i+1}: ')))

print('Original array:', x)

# Bubble sort
swapped = True
while swapped:
    swapped = False
    for i in range(n-1):
        if x[i] > x[i+1]:
            x[i], x[i+1] = x[i+1], x[i]
            swapped = True

print('Sorted array:', x)



# understanding assert statements
x = int(input('Enter a num greater than 0: '))
try:
    assert (x > 0)
    print('U entered: ',x)
except AssertionError:
    print("Wrong input entered")


# program to access each element of a string in forward and reverse order using while loop
str = 'Core Python'
# access each character using while loop
n = len(str) # n = no. of chars in str
i = 0 # i = 0,1,2,... n-1
while i < n:
    print(str[i], end=' ')
    i += 1

print() # put cursor into next line
# access in reverse order
i = -1 # i = -1,-2,-3,... -n
while i >= -n:
    print(str[i], end=' ')
    i -= 1

print() # put cursor into next line
# access in reverse order using negative numbers
i = 1 # i = 1,2,... n-1
n = len(str) # n = no. of chars in str
while i <= n:
    print(str[-i], end=' ')
    i += 1


# to know whether sub string is in main string or not
str = input('Enter main string: ')
sub = input('Enter sub string: ')
if sub in str:
    print(sub+' is found in main string')
else:
    print(sub+' is not found in main string')


# Program to reverse a number without library function
num  = int(input("Num: "))
rev = 0
is_negative = False

if num < 0:
    is_negative = True
    num = abs(num)

while num > 0:                # 234                 23      2     
    rem = num % 10            # 234 % 10 = 4        3       2 % 10 = 2
    rev = (rev * 10) + rem    # 0 * 10 + 4 = 4      43      43 * 10 + 2 = 432
    num = num // 10           # 234 // 10 = 23      2       2 // 10 = 0

if is_negative:
    rev = -rev

print("Reverse", rev)


# Program to see if the entered number is armstrong or not 
num = int(input('Enter num: '))
sum = 0
temp = num

while temp > 0:             # 153                 15                  1
    digit = temp % 10       # 153 % 10 = 3        15 % 10 = 5         1 % 10 = 1
    sum += digit ** 3       # 0 + 3**3 = 27       27 + 5**3 = 152     153 + 1**3 = 153
    temp //= 10             # 153 // 10 = 15      15 // 10 = 1        1 // 10 = 0

if sum == num:
    print(num,'is armstrong number')
else:
    print(num,'is not armstrong number')



# Program to unserstand classes and objects
class House:
    def __init__(self, num_rooms, kitchen_size):
        self.num_rooms = num_rooms
        self.kitchen_size = kitchen_size

    def turn_on_lights(self):
        print("Turn on lights")

    def open_door(self):
        print("Open the door")

# Create an instance of the House class with specified attributes
my_house = House(3, "large")

# Call methods on the instance
my_house.turn_on_lights()
my_house.open_door()



# Program to demonstrate encapsulation and name mangling in a class
class Myclass:
    def __init__(self):
        # Initialize instance variables
        self.x = 1
        self.__y = 2  # Name mangling for private attribute
    
    def display(self):
        # Display values of instance variables
        print(self.x)
        print(self._Myclass__y)  # Access private attribute using name mangling

print("Accessing variables through methods:")
m = Myclass()  # Create an instance of Myclass
m.display()    # Call the display method to access and display values

print("Accessing variables through instance:")
print(m.x)  # Access x directly using the instance
print(m._Myclass__y)  # Access __y using name mangling
