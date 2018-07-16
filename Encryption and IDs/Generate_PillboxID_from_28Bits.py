rmap = [10,9,4,17,15,1,21,19,0,7,22,12,26,5,16,6,20,3,24,11,25,8,14,2,23,18,27,13]

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