# 20-03-2024.

#2) find the uncommon words from 2 strings.

'''
s1 = "Hello how are you"
s2 = "Hello how is "
s1 = s1.split(" ")
s2 = s2.split(" ")
for val in s1:
    if val not in s2:
       print(val)
for val in s2:
    if val not in s1:
       print(val)
'''


# 3). write a code print the 8th fibanochi number .
#0,1,1,2,3,5,8


'''

num = 8
n1 = 0
n2 = 1

for val in range(num):
    ans = n1+n2
    print(ans)   -------here print in the for loop.
    n1 = n2
    n2 = ans 
'''
### or

'''
num = 8
n1 = 0
n2 = 1

for val in range(num):
    ans = n1+n2
   
    n1 = n2
    n2 = ans 
print(ans)  ----> hare print val out sude the for loop.

'''



## constructors
#  Eg : 2
'''
class profile:
    def __init__(self):
        print("hello world")

obj = profile()
obj.__init__()

'''
# Eg : 3
# parameterised consrtuctor
'''
class profile:
    def __init__(self, id, name,age):
        print(id, name, age)
obj = profile(1, "krish" , 20)
'''
# Eg : 4
'''
class c1:
    email = "kri@gmail.com"
    def m1(self):
        name = "krish"
        place= "ATP"
        print(name,place)
        print(self,email)
        
object = c1()
object.m1()
'''
# Eg : 5
'''
class c1:
    def m1(self):
        name = "sid"
        age = 20
     def display(self):
         print(name,age)
         print(self.name,self.age)
         print(self.m1())
    

object = c1()
object.display()


'''


# Eg :6

# To use the variable inside the constructor in another method
'''
class class1:
    
    def __init__(self):
       self.name = "sid"
       self.email = "kri@gamail.com"
       # return name,email# error---> cannot use return with consrtuctor
    def display(self):
        print(self.name, self.email)



c1 = class1()
c1.display()
'''

# -----> Inheritance.
# the procees of utilising the method and attributes of parent class
#throught the object of child class it is called as inheritance.

  #  5 types of inheritance
'''
  single inheritance
  multilevel inheritance
  multiple inheritance
  hybrid inheritance
  heirarichal inheritance
'''
# ***single inheritance

# it has only one parent class and only one child class
#  eg : 1

'''
class parent:
    def m1(self):
        print("Iam perent class")

        

class child(parent):
    def m2(self):
        print("Iam child class")
obj = child()
obj.m1()
'''
   # Eg : 2
'''  
class c1:
    def __init__(self):
        print("Iam consructor from parent class")

class child1(c1):
    pass
obj = child1()

'''


# Eg : 3
'''
class parent:
    name = "krish"

class child(parent):
    def display(self):
        print(self.name)
d = child()
d.display()

'''
 #### or

'''
class parent:
    name = "krish"

class child(parent):
    name = "name1" --------->
    def display(self):
        print(self.name)
d = child()
d.display()
'''

#**** multilevel inheritance.


#  Eg :
'''
class voice:
    def sound(self):
        print("All the animals have their own voices")

class dog(voice):
    def dog_voice(self):
        print("bark")
class cat(dog):
    def cat_voice(self):
        print("meow")

class parrot(cat):
    def parrot_voice(self):
        print("speak")

all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
'''

## Eg :2
'''

class Honda_city:
    def engine_spacs(self,cc,Hp,torque,fuel_type,num_of_piston):
        print(cc,Hp,torque,fuel_type,num_of_piston)

    def honda_city_body-specs(self,color,weight,height,length,vehicle_type):
        print(color,weight,height,length,vehicle_type)



class amaze(Honda_city):
    def amaze_engine_spacs(self,cc,Hp,torque,fuel_type,num_of_piston):
        print(cc,Hp,torque,fuel_type,num_of_piston)
    def amaze_city_body-specs(self,color,weight,height,length,vehicle_type):
        print(color,weight,height,length,vehicle_type)
    
'''

#  it has multiple psrent and child







'''

child while_petrol:
    def function_w(self):
        print("used to airplans")


class organic_petrol:
    def fumction_o(self):
        print(
'''


# ! Eg:2
            
# MRO --> Method resolution Order
'''           
class addition:
    def add(self, a, b):
        print(a+b)
        
    def mul(self, a, b):
        print(a%b)
        
class subract:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subract, multiply):
    def div(self, a, b):
        print(a/b)
        
calc = division() 
# calc.add(3, 4)
calc.mul(4, 2)
'''


# Heirarical inheritance .
# The one parent class will asct as parent for all the child classes.

'''
class catagory:
    def weight(self, weight):
        print("weight")
    def display(self,color,taste):
        print(color, taste)

class Tomato:
    def tomaoto_spaces(self):
        color="black"
        taste = "neutral taste"
        self.display(color,taste)


class carrot (catogory):
    def carrot_specs(self):
        color="green"
        taste = "sweet"
        self.display(color,taste)
        

c = carrot()
c.carrot_specs()
c.weight("30gms")

t = Tomato()
t.tomato_specs()
t.weight("20gms")

'''

#**** Hybrid inheritance.

#The combination of above 4 inheritance is called Hybrid inheritance

'''
class c1:
    def m1(self):
        print("class")

class c2(c1):
    def m2(self):
        print("class2")

class c3(c2):

    def m3(self):
        print("class 3")

class c4(c2):

    def m4(self):
        print("class 4")


class c5(c4):

    def m5(self):
        print("iam me from c4")

class c6(c5,c3):

    def m6(self):
        print("class 4")

obj = c6()
obj.m3()
'''
#----> polymorphism.
#poly - many,morph ---> form
'''
A function which has the ability to perform more than 1 functionality
then it is considered to be as polymorphism
'''
# *** polymorphism in builtin functions
'''
#len() ----> which is used to find the length of list,tuple,dict etc..
#max()
#min()
#count()
#pop()
#and more...
'''

#  *** polymorphism in operators .

# +
# print(8+8)
# print("k"+'1')
#print([1,2,3]+[5,6])



# *
'''
print(6*7)
l1 = {1,2,3,4,5,6}
print(*l1)
def f1(*args)
l1 = [1,2,3,4]
print(l1*10)


polymorphism in classes
we can achive polymorphism in 2 ways
1)method overloading ---> it is not posssible in python
2) method overriding
'''

#1) Tasks
#d1 = {"shirt": 1000,"pant": 1500, "shoes":"900","handkey":30}
#1) find the min ans max priced product
#2) find the product starts with 's' and 's'



#2) find the n =67,is strong number or not


#3) l1 = [1,2,3,4,5,6]
# n=2--->[5,6,1,2,3,4]
# n=3--->[4,5,6,1,2,3]




























