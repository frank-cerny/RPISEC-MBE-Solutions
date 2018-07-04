# Lab1A Helpers

# get the high 32 bits after a 32 bit by 32 bit
# multiplication
def getHigh32BitsFrom64Bits(number):
    # not sure if a mask is neccessary here or not
    # mask = 0x00000000ffffffff
    # must reset equality for it to stay shifted
    number = number >> 32
    # & keeps only the first 32 bits of the shifted number
    # return number & mask
    return number

def getOriginalXor(userName):
    char = userName[3]
    xor = ord(char) ^ 0x1337
    xor = xor + 0x5EEDED
    return xor

def loop(userName, originalSum):
    orgSum = originalSum
    for i in range(len(userName)):
        # var1 = eax, var2 = edx, follows the psuedocode
        char = userName[i]
        var1 = ord(char) ^ orgSum
        var2 = var1
        temp1 = 0x88233b2b
        var1 = var2
        var1 *= temp1
        high32Bits = getHigh32BitsFrom64Bits(var1)
        var1 = var2
        var1 = var1 - high32Bits
        # use bitshifting to avoid float division, decimal places cause overestimation
        var1 = var1 >> 1
        var1 = var1 + high32Bits
        var1 = var1 >> 10
        var1 = var1 * 0x539
        var2 = var2 - var1
        var1 = var2
        orgSum = orgSum + int(var1)
    return orgSum

def main():
    userName = "helper"
    orgSum = getOriginalXor(userName)
    serial = loop(userName, orgSum)
    print('Serial =  %d ' % (serial))
    return serial
        




