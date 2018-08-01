#map = [8,5,23,17,2,13,15,9,21,1,0,19,11,27,22,4,14,3,25,7,16,6,10,24,18,20,10,26]

ID = int(input("Input the ID\n"))
bits = ""
while ID != 0:
    if ID & 1: bits = "1" + bits
    else: bits = "0" + bits
    ID = ID >> 1
if len(bits) <= 28:
    while len(bits) < 28:
        bits = "0" + bits
    count = 0
    code = ''
    while count < 28:
        code = code + bits[count]
        count += 1
    print(code)
else: print("Code Length Error")