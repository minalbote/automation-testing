# calculator

# addition method
def add(value1,value2):
    sol = value1+value2
    return sol
    
# substraction method
def sub(value1,value2):
    sol = value1+value2
    return sol
   
# multiplication method
def mul(value1,value2):
    sol = value1*value2
    return sol
     
# divison method
def div(value1,value2):
    sol = value1/value2
    return sol



x = int(input("Enter first value: "))
choice = input()
y = int(input("Enter second value: "))

if choice == "+":
    print(add(x,y))
if choice == "-":
    print(sub(x,y))
if choice == "*":
    print(mul(x,y))
if choice == "/":
    print(div(x,y))