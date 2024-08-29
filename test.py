x = "Zara"
y =  10
z =  10.10

print(type(x))
print(type(y))
print(type(z))


x = str(10)    # x will be '10'
y = int(10)    # y will be 10 
z = float(10)  # z will be 10.0

print( "x =", x )
print( "y =", y )
print( "z =", z )


age = 20
Age = 30

print( "age =", age )
print( "Age =", Age )


# def sum(x,y):
#    sum = x + y
#    return sum
# print(sum(5, 10))


def sum_of_digits(num):
    sum_digits = sum(int(digit) for digit in str(num))
    if sum_digits >= 10:      
        return sum_of_digits(sum_digits)
    else:      
        return sum_digits
num = 897
result = sum_of_digits(num)
print(result) 




for i in range (5):
    print(i)


a = 21
b = 10
c = 0

c = a + b
print ("a: {} b: {} a+b: {}".format(a,b,c))



name=str(input())
print('my name is',name)


def weekday(n):
   match n:
      case 0: return "Monday"
      case 1: return "Tuesday"
      case 2: return "Wednesday"
      case 3: return "Thursday"
      case 4: return "Friday"
      case 5: return "Saturday"
      case 6: return "Sunday"
      case _: return "Invalid day number"
       
print (weekday(3))
print (weekday(6))
print (weekday(7))


def greeting(words):
    match words:
        case [time,name]:
            return f'GOOD {time} {name}'
        case [time,*names]:
            msg=''
            for name in names:
                msg+=f'good {time} {name}\n'
                return msg



print (greeting(["Morning", "Ravi"]))
print (greeting(["Afternoon","Guest"]))
print (greeting(["Evening", "Kajal", "Praveen", "Lata"]))


var ={1:10,2:30,3:40}
print(1 in var)
print(10 in var)


def num(n):
    if(n>10):
        value=sum(int(i) for i in str(n))
        if(value>10):
            num(value)
        else:
             print(value)
        
num(879)

   


def weekday(n):
    match n:
        case 0: print('zero')
        case 1: print('one')
        case 2: print('two')
        case 3: print('three')
        case _: print("number")


weekday(0); 



def add(*args):
    s=0
    for i in args:
        s=s+i
    return s
    
result=add(1,1,2,3)
print(result)

import math
print("square root of 100:",math.sqrt(100))

s1 = "word"
print("original string:",s1);

l1=list(s1)
l1.insert(3,'l')
print(l1)

s2=''.join(l1)
print(s2)





mystring="my name is  vinay gupta"
vowels="aeiou"
count=0
for x in mystring:
    if x.lower() in  vowels:
        count+=1
print(count)

import copy
l1=[1,2,3,4]
l2=copy.copy(l1)
l2[0]=100
print(l2)
print(l1)




l1=[11,2,3,4,5,64,5,2,3,1]
l2=[]
for x in  l1:
    if x not in l2:
     l2.append(x)

print(l2)

print(sum(l1))



import random

l1=[]
for i in range(5):
    x=random.randint(0,100)
    l1.append(x)
print(l1)


### tuples
t1=(1,2,3,45,4)
t2=()
for x in t1:
    if x not in t2:
         t2+=(x, )
print(t2)


##sets

l1=[1,2,3]
l2=[1,2,3]

nest=[(x,y) for x in l1 for y in l2]
print(nest)



import itertools

# Defining a set
original_set = {1, 2, 3, 4}

# Checking if {1, 2} is a subset of the original set
is_subset = {1, 2}.issubset(original_set)
print("{1, 2} is a subset of the original set:", is_subset)

# Generating all subsets with two elements
subsets_with_two_elements = [set(subset) for subset in itertools.combinations(original_set, 2)]
print("Subsets with two elements:", subsets_with_two_elements)


# we can use add() and update() to add a element to set

# we can use remove() and discard() and pop() to remove a element from set and clear() to clear set 


s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}


# s1.difference_update(s2)
# print ("s1 after running difference_update: ", s1)

result_set = s1 ^ s2
print("Resulting Set:", result_set)


s1.intersection_update(s2)
print("Set 1 after keeping only common items:", s1)


s3 = s1.intersection(s2)
print ("s3 = s1 & s2: ", s3)

#dictionary

student_info = {
    "name": "Alice",
    "age": 21,
    "major": "Computer Science"
}


all_keys = student_info.keys()
print("Keys:", all_keys)  



person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Updating multiple values
person.update({'age': 26, 'city': 'Los Angeles'})
print(person)



# adding two dict


marks = {"Savita":67, "Imtiaz":88, "Laxman":91, "David":49}
print ("marks dictionary before update: \n", marks)
marks1 = {"Sharad": 51, "Mushtaq": 61, "Laxman": 89}
newmarks = marks | marks1
print ("marks dictionary after update: \n", newmarks)

#arrays

import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
print (type(a), a)


a.insert(1,100)
for x in a:
    print(x)

a.append(10)

a.insert(3,90)

a1=arr.array('i',[9,8,7,6,5])
a.extend(a1)

a.remove(100)




