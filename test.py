print("hello world")

# comment
# js - let, const,var
x = 5
y = "hello"
print(x, y)

# variable types
# js =array
list = [1,2,3,4]
list.append(5)
print(list)
list.remove(1)
print(list)

# dict = {key : value}
dict = {"name": "John", "age": "30"}
print(dict)
dict["country"] = "usa"

# remove
dict.pop("name")
print(dict)

dict.clear()
print(dict)

# for loop
# for JS- (let i=0,i=<5,i++) {console.log(i)};
# no {} for pythonS
for i in range(5):
    print(i)  

# while loop
# for JS - while(i < 5) {console.log(i); i++; }
i = 0
while i < 5:
    print(i)
    i += 1

# if else statement
# for JS - if (x > 0){console.log("x is positive");} else if (x < 0) {console.log("x is negative");} else {console.log("x is zero");}
x = 0
if x > 0:
    print("x is a positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# function
# for JS - function add(a,b) {return a+b; }
def add (a,b):
    return a + b
print(add(5,10))

# create input from user
# name = input("enter your name: ")
# print("hello " + name)

# number = input("enter a number: ")
# print("the number is " + number)

def print_menu():
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. exit")

print_menu()

choice = input("enter choice: ")
num1 = float(input("enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
result = 0
if choice == "1":
    result = num1 +num2
elif choice == "2":
    result = num1 - num2
elif choice == "3":
    result = num1 * num2
elif choice == "4":
    if num2 == 0:
        print("cannot divide by 0")
        exit(1)
    else:
        result = num1 / num2
elif choice == "5":
    print("exiting...")
else: 
    print("invalid choice")
    exit(1)
print("result: ",result)