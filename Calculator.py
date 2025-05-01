def add(a, b):
    return a+b
def sub(c, d):
    return d-c
def multi(a, b):
    return b*a
def division(a,c):
    if a==0:
        return "error, pls try again" 
    else:
        return c/a
# Writing simple calculator program
print("my simple calculator")
print("Arithemetic operation: addition, subtraction, multiplication and division")
num1 = float(input("enter the first num: "))
num2 = float(input("enter the second num: "))
operation = input("enter the operation").lower()

if operation=="add":
    result = add(num1, num2)
elif operation=="sub":
    result =sub(num1, num2)
elif operation=="division":
    result = division(num1, num2)
elif operation=="multi":
    result =multi(num1, num2)
else:
    result="invalid operation"
print("result :" ,result)