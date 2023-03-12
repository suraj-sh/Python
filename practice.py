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
for n in range(1, numr):
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

# Fibonacci series
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(1):
    print(fib(i), end=", ")
print(fib(1))   