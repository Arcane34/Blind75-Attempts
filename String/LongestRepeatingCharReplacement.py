
string = 'AABABBA'
currentLetter= ''
currentLength = 0
k = 1

maxLetter= ''
maxLength = -1
for i in range(len(string)):
    if i == 0:
        currentLetter = string[i]
        currentLength = 1
    elif string[i] == currentLetter:
        currentLength += 1
    elif string[i] != currentLetter:
        if currentLength > maxLength:
            maxLength = currentLength
            maxLetter = currentLetter

        currentLetter = string[i]
        currentLength = 1
    
print(maxLength, maxLetter)