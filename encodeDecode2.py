import base64
'''
처음 시작할 때 입력받는 문장은 alphanumeric이다. 
'''
string = input("Please write alphanumeric sentence here: ")

def convert(toEnc):
    """
    toEnc : 변환 후 문자열의 인코딩 - 'alpha', 'ascii', 'bin', 'oct', 'hex', 'base64'

    """ 
    global string

    ascii = ' '.join(str(ord(char)) for char in string)
    bin = ' '.join(str(format(ord(char), '#b')) for char in string)
    oct = ' '.join(str(format(ord(char), '#o')) for char in string)
    hex = ' '.join(str(format(ord(char), '#x')) for char in string)
    sixtyfour = base64.b64encode(string.encode('utf-8'))
    print(sixtyfour)

    if toEnc == 'alpha':
        return string
    elif toEnc == 'ascii':
        return ascii
    elif toEnc == 'bin':
        return bin
    elif toEnc == 'oct':
        return oct
    elif toEnc == 'hex':
        return hex
    elif toEnc == 'base64':
        return sixtyfour
    else:
        pass



while True:
    tE = input("\nTo what type do you want to change your sentence? Choose from alpha, ascii, bin, oct, hex, base64: ")
    encoded = convert(tE)
    print("\nHere is your encoded text...\n")
    print(encoded)
    print('')
    endOrContinue = input("Would you like to continue? Y/N: ")

    if endOrContinue == 'Y' or endOrContinue == 'y':
        pass
    elif endOrContinue == 'N' or endOrContinue == 'n':
        break