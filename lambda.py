x = lambda a :a + 10
print(x(5))

a = lambda a,b,c : a * b * c
print(a(4,5,6))

def lambda_function(a,b):
    return a + b
print(lambda_function(4,5))

x = 0
for x in range(1,13):
    if x > 0:
        result = x * 5
        print(result)
        x = x + 1
def myfunction(n):
    return lambda a : a * n
mydoubler = myfunction(2)
mytripler = myfunction(2)

print(mydoubler(11))
print(mytripler(12))

def mytest(c):
    return lambda x : x * c
mytripler = mytest(4)
print(mytripler(12))
a = 0
for x in range(2):
    if lambda x : x + 2:
        result = 3 + 2
        print(result)
        a = a + 1

def prime(n):
    if (n > 0):
        result = n + (prime(n - 1))

    else:
        result = 0
    return(result)
print(prime(8))

def bool_to_string(flag):
    fl_str = str(flag)
    return fl_str
print(bool_to_string(True))

def bool_string(flag):
    if flag == True:
        fl_str = str(flag)
        return fl_str
print(bool_string(True))

x = lambda x : x + 20
print(x(5))
x = 0
count = 0
for x in range (8):
    if lambda x : x + 7:
        result = 8 + 7
        print(result)
        count= count + 1
class myclass:
    x = 5

p1 = myclass()
print(p1.x)
print(type(myclass))

class person:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = 4.5

    def myfunc(self):
        print("my name is " + self.name)
        print("I am " + str(self.age))
        print("I am also " + str(self.height))

p1 = person("kodjo", 30,4.5)
p1.myfunc()





   




    

