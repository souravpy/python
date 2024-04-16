#1
name = input("paitent's name ")
age = input("paitent's age ")
gender= input("paitent's gender ")
print("paitent's information is: ", name, age, "years", gender)

#2
Fahrenheit= int(input("Please enter a Fahrenheit temperature value: "))
Celsius = ((Fahrenheit-32)*5)/9.
print("The converted Celsius temperature is ", Celsius)

#3
total_sum = 1.0
for i in range(3, 100):
    total_sum += 1/i  
print("The sum of the series is:", total_sum)


