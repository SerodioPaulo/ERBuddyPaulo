

mode = input("Input Code(0) or ID(1)?   ")
print(mode)

map = [8,5,23,17,2,13,15,9,21,1,0,19,11,27,22,4,14,3,25,7,16,6,10,24,18,20,10,26]
rmap = [10,9,4,17,15,1,21,19,0,7,22,12,26,5,16,6,20,3,24,11,25,8,14,2,23,18,27,13]

if mode == '0':
    code = input("Input the Code of 28 0/1 bits\n----------------------------\n")
    if len(code) == 28 and code.count('1') + code.count('0') == 28:
        count = 0
        ID = 0
        while count != 28:
            if code[rmap[count]] == '1': ID +=1
            ID = ID << 1
            count += 1
        ID = ID >> 1
        print(ID)

if mode == '1':
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