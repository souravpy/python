#----------------------------------------------------------------------------
#class definition block

from codecs import getencoder


class comp:
        def conf(self):
                print("16core")

#-----------------------------------------------------------------------------                
#object definition block
#class calling block

ryzen = comp()  # here ryzen is an object belonging to the class comp
                # here object doesnt have any argument
intel = comp()  # intel belongs to class
print(type(ryzen)) 

#  to use a method from a class use 
# "method.class(object)" 
# "object.method()", just as same 

#-----------------------------------------------------------------------------
#create classes Person and Employee
#make Employee inehrit methods from the Person Class
#think about attributes unique attributes for person and employee

class Person:
        def __init__(self):
                self.age = age
                #self.gender = gender
                #self.name = name
                #initiating objects
                #providing defaul value
                #init contains all the variables to be used by the different methods

                #init is called immediately after a new object is created

        def name(self):
                #for assignin the name varaible
                name = input("enter the name of the perosn")
                


#        def iq(self):
#                s