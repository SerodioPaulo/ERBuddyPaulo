import random

# Get the pillboxID from the URL

# Get the encryptedKey from the JSON

#The URL will come like this: requests.post("http://127.0.0.1:8000/erbuddyapi/registerpillbox/" + str(pillboxID), data = {'pillBox':{'pill-key': encryptedKey}})

# Get the counter, seed, startIndex, and endIndex from the master seed table

# Get the pillboxKey from master pillbox table

random.seed(seed[startIndex:endIndex])

holdCounter = counter

decodedKey = ""

count = 0
while count != counter:
    random.randrange(0,94)
    count += 1

count = 0
while count < len(pillboxKey):
    decodedKey = decodedKey + chr(((ord(encryptedKey[count]) + 62 - random.randrange(0,94))%94) + 32)
    counter += 1
    count +=1

if decodedKey == pillboxKey: #Success!
else: counter = holdCounter #Failure!