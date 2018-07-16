import random
import requests

pillboxID = 134854781
pillboxKey = "TestingKey99823" #Must consist of ASCII chars between 32 and 126
seedMaster = 'xMW59kR4JvFf9iW3djWxIPubljc2Up8FTkjL3TWJHGO1eXQ9oeC7EEd8haSC08kmlbaKC4MeoGz9ET5zksMYBI9f9a9Ne1gB0LMx'
seedCounter = 0

holdCounter = seedCounter
seedCurrent = seedMaster[startIndex:endIndex]
print("Current seed: " + seedCurrent)

#Direction of Shift: Pillbox = 1, Server = -1

random.seed(seedCurrent)

count = 0
while count != seedCounter:
    random.randrange(0,94)
    count += 1

encodedKey = ""
count = 0
while count < len(pillboxKey):
    encodedKey = encodedKey + chr( ( ord(pillboxKey[count] - 32 + random.randrange(0,94) ) % 94 ) + 32 )
    seedCounter += 1
    count +=1

print("http://104.236.194.242/erbuddyapi/registerpillbox/" + str(pillboxID) + '/' + encodedKey)
#This is where you would send the request to the database, which will respond with Success or Failure

if(Failure): seedCounter = holdCounter
