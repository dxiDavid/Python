randomString = str("Hello world string with some random words")
randomNumber = int(50)

print(randomString[3], len(randomString), randomNumber)
print("Hello" in randomString)

convertedRandomNumber = str(randomNumber)
print(convertedRandomNumber, type(convertedRandomNumber))
print(randomString[0:6])
print(randomString[6:12].upper(), randomString.replace("o", "0").capitalize())

formatString = f"Hello World string with some random words and a number which is {randomNumber}"
print(formatString)
