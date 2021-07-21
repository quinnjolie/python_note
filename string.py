#string formatting/manipulation
#string is an array of characters/object

#string interpolation
name = "Kodjo"
print(f"My name is {name}")

#string formatting
firstname = "joel"
age = 30
gender = "Male"
print("{0} is a {1} of {2} years old".format
(firstname,gender,age))

#names indexes
mes = "i have a very nice {house}".format(house = "a well known palace house")
print(mes)

#string concatenation
val1 = "i"
val2 = "phone"
val3 = "12 pro"

full = val1 + " " + val2 + " " + val3
print(full)
print(f"{val1} {val2} {val3}")

