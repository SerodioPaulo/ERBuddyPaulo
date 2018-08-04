import random

seedMaster = 'xMW59kR4JvFf9iW3djWxIPubljc2Up8FTkjL3TWJHGO1eXQ9oeC7EEd8haSC08kmlbaKC4MeoGz9ET5zksMYBI9f9a9Ne1gB0LMx'
seedCounter = 0
startIndex = 0
endIndex = 10

seedCurrent = seedMaster[startIndex:endIndex]

def EncryptData(data, seed, counter):
    random.seed(seed)
    c = 0
    while c != counter:
        random.randrange(0,94)
        c += 1
    edata = ""
    c = 0
    while c < len(data):
        edata = edata + chr( ( ( ord(data[c]) - 32 + random.randrange(0,94) ) % 94 ) + 32 )
        counter += 1
        c += 1
    return edata

def DecryptData(edata, seed, counter):
    random.seed(seed)
    c = 0
    while c != counter:
        random.randrange(0,94)
        c += 1
    data = ""
    c = 0
    while c < len(edata):
        data = data + chr( ( ( ord(edata[c]) + 62 - random.randrange(0,94) ) % 94 ) + 32 )
        counter += 1
        c += 1
    return data

#After this decryption, if the pillboxKey does not match, deincrement seedCounter by len(input)

#Usage

ask = input("Type some input:   ")

a = EncryptData(ask, seedCurrent, seedCounter)

print(a)

b = DecryptData(a, seedCurrent, seedCounter)

print(b)