rmap = [18, 20, 23, 24, 4, 1, 21, 15, 2, 19, 27, 16, 10, 5, 7, 0, 8, 6, 22, 3, 17, 25, 12, 14, 13, 26, 11, 9]

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
