# print('whatup!')

# L1 = ["john", 102, "USA"]
# print(type(L1))

# tup = ("apple", "mango", "banana", "orange")
# print(type(tup))
# print(tup)
# # tup[2] = "papaya"

# employee = {"Name": "John", "Age": 30, "Salary": 250000, "Company": "GOOGLE"}
# print(type(employee))
# print("Printing employee data......")
# print(employee)

# # Printing prime number 
# # Method - 1
# min = int(input("Enter the min: "))
# max = int(input("Enter the max: "))
# for n in range(min, max + 1):
#     if n > 1:
#         for i in range(2,n):
#             if (n % i) == 0:
#                 break
#         else:
#             print(n,end=" ")

# # Method - 2
# numr = int(input("Enter range: "))
# print("Prime numbers:",end=" ")
# for n in range(1, numr+1):
#     if n > 1:
#         for i in range(2, n):
#             if (n % i) == 0:
#                 break
#         else:
#             print(n,end=" ")

# # Sorting elements in the list
# # Method - 1
# mylist = [5, 8, 9, 6, 3]

# for i in range(len(mylist)):
#     for j in range(i+1, len(mylist)):
#         if mylist[j] > mylist[i]:
#             mylist[i], mylist[j] = mylist[j], mylist[i]
# print(mylist)

# # Method - 2
# mylist = [2, 5, 7, 5, 3, 4, 5, 2]
# asc = []
# while mylist:
#     min = mylist[0]
#     for i in mylist:
#         if i < min:
#             min = i
#     asc.append(min)
#     mylist.remove(min)
# print(asc)

# # Find maximum number from an array
# arr = [15, 4, 3, 6, 9]
# max = arr[0]
# for i in arr:
#     if i > max:
#         max = i
# print(max)

# # For asending
# mylist = [5, 8, 9, 6, 3]
# new = sorted(mylist)
# print(new)

# # For descending
# mylist = [5, 8, 9, 6, 3]
# new = sorted(mylist, reverse=True)
# print(new)

# # Find duplicate value and sort in descending order
# mylist = [2, 5, 7, 5, 3, 4, 5, 2]

# def duplicate(mylist):
#     empty = []
#     asc = []

#     for i in mylist:
#         if i not in empty:
#             empty.append(i)
    
#     while empty:
#         min = empty[0]
#         for i in empty:
#             if i < min:
#                 min = i
#         asc.append(min)
#         empty.remove(min)
#     return asc  

# ans = duplicate ([2, 5, 7, 5, 3, 4, 5, 2])
# print('Duplicate values are:',ans)

# # to find substring using diffrent functionalities 
# str = 'hello hello whatup hello'
# count = str.count('hello')
# print(count)
# find = str.find('hello')
# print(find)
# index = str.index('hello') # same as find but returns ValueError if string not present
# print(index)
# end = str.endswith('o')
# print(end)
# start = str.startswith('h')
# print(start)

# # Program to find the factorial of a number
# num = int(input("Enter the num: "))
# fact = 1

# for i in range(1, num+1):
#     fact = fact * i
# print(f'The factorial of {num} is {fact}')

# # Find maximum number from an array
# arr = [5, 4, 3, 6, 9]
# max = arr[0]
# for i in arr:
#     if i > max:
#         max = i
# print(max)

# # sorting list in ascending order
# mylist = [5, 8, 6, 3, 9]
# empty = []
# while mylist:
#     min = mylist[0]
#     for i in mylist:
#         if i < min:
#             min = i
#     empty.append(min)
#     mylist.remove(min)
# print(empty)

# # Python program to find second largest number in a list
# list1 = [10, 20, 20, 2, 4, 45, 54, 34, 15]
# # Removing duplicates from the list
# list2 = list(set(list1))
# list2.sort()
# print("Second largest element is:", list2[-2])

# # Fibonacci series
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(6):
#     print(fib(i), end=", ")
# print(fib(i))   

# n = int(input("Enter range: "))
# f1=0
# f2=1
# c=2
# print(f1, f2, end=", ")
# while c<n:
#     f = f1+f2
#     print(f)
#     f1, f2 = f2, f
#     c+=1


# Program to generate Fibonacci series

# def fibonacci(n):
#     a, b = 0, 1
#     fib = [a, b]

#     for i in range(2, n):
#         c = a+b
#         fib.append(c)
#         a, b = b, c
#     return fib

# n = int(input("Enter the range: "))
# print(fibonacci(n))

# for i in range(1, 6):
#     for j in range(1, i+1):
#     # print('* '*(i))
#         print('* ', end='')
#     print()

# class House:
#     def __init__(self, num_rooms, kitchen_size):
#         self.num_rooms = num_rooms
#         self.kitchen_size = kitchen_size

#     def turn_on_lights(self):
#         print(f"Turn on lights")

#     def open_door(self):
#         print("Open the door")

# my_house = House(3, "large")
# my_house.turn_on_lights()
# my_house.open_door()

# class Myclass:
#     def __init__(self):
#         self.x = 1
#         self.__y = 2
#     def display(self):
#         print(self.x)
#         print(self._Myclass__y)

# print("Accessing variables through methods:")
# m = Myclass()
# m.display()

# print("Accessing variables through instance:")
# print(m.x)
# print(m._Myclass__y)

# arrays 
# import array
# from array import *
# a = array('i', [5, 6, -7, 8])
# b = array('u', ['a', 'e', 'i', 'o', 'u'])
# print("The array elements are:")
# for element in a:
#     print(element)
# for ch in b:
#     print(ch)

# from array import *
# arr1 = array('d',[1.5, 2.5, -3.5, 4])
# print('The arr1 elements are:')
# for j in arr1:
#     print(j, end=' ')
# arr2 = array(arr1.typecode, (a*3 for a in arr1))
# print('\nThe arr2 elements are:')
# for i in arr2:
#     print(i, end=' ')

# from array import *
# x = array('i', [10, 20, 30, 40, 50])
# n = len(x)
# print(f"Length of the array is {n}")
# print("using for loop")
# for i in range(n):
#     print(x[i], end=" ")
# print("\nUsing while loop")
# j = 0
# while j < n:
#     print(x[j], end=" ")
#     j+=1 

# n = 50
# for i in range(1,11):
    # print(' '*n, end="")
    # print('* '*(i))
    # print(' '*(n-i) + '* '*(i))
    # n-=1

# a = int(input("Enter the number: "))
# r = 0
# while a!=0:
#     r = r*10 + a%10
#     a = a//10
# print(r)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# def sort_numbers(numbers):
#     even_numbers = []
#     odd_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)
#     return (even_numbers, odd_numbers)
# even_numbers, odd_numbers = sort_numbers(numbers)
# print(even_numbers)
# print(odd_numbers)

# def sort_numbers(numbers):
#     even_numbers = [num for num in numbers if num % 2 == 0]
#     odd_numbers = [num for num in numbers if num % 2 != 0]
#     return (even_numbers, odd_numbers)

# def sort_numbers(numbers):
#     even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#     odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
#     return (even_numbers, odd_numbers)

# my_list = [1, 2, 3, 2, 4, 3, 5, 6, 7, 5, 8, 9, 9]

# # Create an empty list to store duplicate elements
# duplicates = []

# # Create a set to store unique elements
# seen = set()

# # Iterate through each element in the list
# for num in my_list:
#     # If we have already seen this element, it is a duplicate
#     if num in seen:
#         duplicates.append(num)
#     else:
#         seen.add(num)
# print(duplicates)

# from array import *

# # str = input('Enter marks: ').split(' ')
# str = (50, 56, 75, 67, 45)
# marks = [int(num) for num in str]
# sum = 0
# for x in marks: 
#     print(x)
#     sum += x
# print(f'Total marks: {sum}')

# n = len(marks)
# percent = sum / n
# print(f'Percentage: {percent}%')

# from array import *

# arr = array('i', [1, 2, 3, 4, 2, 4, 5, 1, 6, 2, 6])
# freq = {}
# for num in arr:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
    
# for num, count in freq.items():
#     print(f"NUM: {num} | COUNT: {count} ")

# Sorting an array using Bubblesort
# from array import *
# Create an empty array to store integers
# x = array('i', [])

# Store elements into the array x
# print('No. of elements ', end='')
# n = int(input())    # accept input into n

# for i in range(n):  # repeat for n times
#     print('Enter element: ', end='')
#     x.append(int(input()))  # add the element to the array x

# print('Original array: ', x)

# # Bubble sort
# flag = False    # when swapping is done, flag becomes True
# for i in range(n-1):    # i is from 0 to n-1
#     for j in range(n-i-1):  # j is from 0 to one element lesser than i
#         if x[j] > x[j+1]:   # if 1st element is bigger than the 2nd one
#             t = x[j]    # swap j and j+1 elements
#             x[j] = x[j+1]
#             x[j+1] = t
#             flag = True # swapping done, hence flag is true 
#     if flag == False:   # no swapping means array is sorted order
#         break   # come out of inner for loop
#     else:
#         flag = False    # assign initial value to flag
# print('Sorted array: ', x)    

# from array import *

# # Create an empty array to store integers
# x = array('i', [])

# # Store elements into the array x
# n = int(input('No. of elements: '))
# for i in range(n):
#     x.append(int(input(f'Enter element {i+1}: ')))

# print('Original array:', x)

# # Bubble sort
# swapped = True
# while swapped:
#     swapped = False
#     for i in range(n-1):
#         if x[i] > x[i+1]:
#             x[i], x[i+1] = x[i+1], x[i]
#             swapped = True

# print('Sorted array:', x)