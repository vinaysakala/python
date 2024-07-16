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



