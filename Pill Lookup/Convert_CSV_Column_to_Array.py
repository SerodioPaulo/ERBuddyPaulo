import csv
import sys

file = open("testing.txt","w") 

pilltxt = list(csv.reader(open('PillLookup.csv', 'r'), delimiter='\t'))
print("Which column?")
column = int(input())

list = '["'
try:
	index = 1
	while True:
		list = list + str(pilltxt[index][column]) + ';",";'
		index += 1
except IndexError:
	list = list + '"]'

file.write(list)
file.close 
