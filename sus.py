def summ():
        a=int(input("enter the number a"))
        b=int(input("enter the numebr b"))
        c=a+b
        return c
def main():
        caller=int(input("input any number to use sum function"))
        if type(caller)==int:
                print(summ())
        else:
                main()
