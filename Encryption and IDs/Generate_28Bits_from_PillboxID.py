map = [15, 5, 8, 19, 4, 13, 17, 14, 16, 27, 12, 26, 22, 24, 23, 7, 11, 20, 0, 9, 1, 6, 18, 2, 3, 21, 25, 10]

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
        code = code + bits[map[count]]
        count += 1
    print(code)
else: print("Code Length Error")
