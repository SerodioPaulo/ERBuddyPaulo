import csv
pilltxt = list(csv.reader(open('PillLookup.csv', 'r'), delimiter='\t'))

inputs = []
first = []
firstp = []
matches = []
matchcheck = 0
matchnum = 0
results = []
print('Enter entries until done, then enter')

while True:
	ask = input()
	if ask == "":
		if len(inputs) != 0:
			break
	else:
		inputs.append(str(ask).lower())

count = 0
while count != len(inputs):
	first.append(inputs[count][0])
	count += 1

try:
	index = 0
	while True:
		data = str(pilltxt[index][22]).lower()
		try:
			if data: #If data is empty throw an index error
				datacount = 0
				firstcount = 0
				try:
					while True:
						if data[datacount] == first[firstcount]:
							#print("prime match in row",index,":",data)
							matchcheck = 1;
							break
						firstcount += 1
				except IndexError:
					matchcheck = 0
				datacount= 1
				firstcount = 0
				if matchcheck == 0:
					try:
						while True:
							if data[datacount-1] == ";" and data[datacount] == first[firstcount]:
								#print("post match in row",index,":",data)
								matchcheck = 1
								break
							firstcount += 1
							if firstcount == len(first):
								firstcount = 0
								datacount += 1
					except IndexError:
						datacount = 0
				if matchcheck == 1:
					count = 0
					matchcount = 0
					while True:
						if inputs[count] in data:
							matchcount += 1
						count += 1
						if count == len(inputs):
							break
					if matchcount == len(inputs):
						results.append(index)
						print("[",matchnum,"]  ",str(pilltxt[index][23]),str(pilltxt[index][15]),":",data)
						matchnum += 1
		except IndexError: #If data is empty
			index = index
		index += 1
except IndexError:
	print("\nThere were",matchnum,"results. Enter a number for more detail")
ask = input()
if ask.isnumeric:
	index = results[int(ask)]
	print("\n",str(pilltxt[index][23]),str(pilltxt[index][15]),"\n",str(pilltxt[index][1]),"mm",str(pilltxt[index][3]),str(pilltxt[index][2]))

