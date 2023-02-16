m = int(input("enter the month number: "))
monthname=["jan","feb","march","april","may","june","july","august","sept","oct","nov","dec"]

print("the month is: ", monthname[m-1])
#since index starts from zero, answer was inaccurate

if (m%2 == 0):
    if (m == 2):
        print("number of days is = 28")
    else:
        print("number of days is = 30")
else:
        print("number of days is = 31")

