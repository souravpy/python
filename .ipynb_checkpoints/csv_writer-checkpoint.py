import csv

input_text = open("input.txt", "r")
output_text = open("output.csv", "w")
writer = csv.writer(output_text)

for word in input_text:
    data = word.strip().split(",")
    writer.writerow(data)
    input_text.close() 
    output_text.close() 
