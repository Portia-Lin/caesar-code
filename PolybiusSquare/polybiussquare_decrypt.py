matrix = [['M', 'A', 'T', 'R', 'I'],
          ['X', 'B', 'C', 'D', 'E'],
          ['F', 'G', 'H', 'K', 'L'],
          ['N', 'O', 'P', 'Q', 'S'],
          ['U', 'V', 'W', 'Y', 'Z']]

matrixHeight = len(matrix)
matrixWidth = len(matrix[0])

def getCryptoChar(char):
    for indexHeight in range(0, matrixHeight):
        for indexWidth in range(0, matrixWidth):
            if char == matrix[indexHeight][indexWidth]:
                return matrix[(indexHeight - 1) % matrixHeight][indexWidth]
    return char
    pass

def decryption(messages):
    newMessage = ""
    for messageIndex in range(0, len(message)):
        newMessage += getCryptoChar(message[messageIndex])
    return newMessage

print("Start!")
message = input("Повідомлення: ").upper()
result = decryption(message)
print("Розшифроване повідомлення:")
print(result)
