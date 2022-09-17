print("hello world im sobby")
class register():
        def __init__(self, name, age):  #for initializing objects
                self.name= name         #initializing the attributes
                self.age= age           #objects have attributes
        def display_detail(self):       #objects belong to a class
                print("name is {self.name}, age is {self.age}")
        def add_db(self):
                pass
stud1= register("baka", 19)
stud2= register("sosy", 2)

stud1.display_detail()

#--------------------------------------------------------------------------------

class Comp():
        def config(self):
                print('sussy, baka')

a=8
print(type(a))

com1=Comp()
print(type(com1))
#datatype of com1 is __main__.Comp
#com1 belongs to Comp class

#---------------------------------------------------------------------------------

#String format() Method  
#string.format(value1, value2...)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)

#---------------------------------------------------------------------------------




class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(abc):
    print("Hello my name is " + self.name)

p1 = Person("John", 36) #here were defining an object p1 beleonging to class Person
                        #holding values jhn,38 being passed to __init__ to initialize 

p1.myfunc()             #p1 object (belonging to person class) accesing myfunc attribute in class 