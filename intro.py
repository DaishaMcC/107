print("hello world!")
# creating variables in python
# JS let or const, boolean or all other ones
name = "Daisha"
last_name = "McCutcheon"
age = 30
found = True
total = 12.99
print(name + last_name + " is " + (age))

#if /else statement
#if (age < 100){console.log("no worries you're not that old")}
if age < 100:
    print("don't worry you're not that old")
elif age > 100:
    print("congrats you're a century")
else:
    "I don't know how you got here"

    print("I'm outside of the if statement")

#functions
#function name_of_the_function() -->this is JS
def say_hello():
    print("hello there!")

def say_good_bye(name):
    print("Good bye "+ name)

def test(name, age, country):
    print("hello my name is " + name + " i have " + str(age) + " years old and i'm from " + country)

#call the function
say_hello()
#name = "Daisha"

say_good_bye(name)
test(name,age, "United States of America")

#create a function that prints "hello my name is" age "and im from" country