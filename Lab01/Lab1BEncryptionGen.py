# xor a with b and return the resulting character
# a is a number in hex format and b is a character
def xor(a, b):
    return chr(a ^ ord(b))


string = "Q}|u`sfg~sf{}|a3"

# xor the string with a number
def xorString(key, string):
    newString = list()
    for i in range(len(string)):
        xoredChar = xor(key, string[i])
        newString.append(xoredChar)
    return newString


    
    
    
