def convert(string,fromEnc,toEnc):
    """
    string : 변환하고자 하는 문자열
    fromEnc :  원래 문자열의 인코딩 - 'alpha', 'ascii', 'bin', 'oct', 'hex'
    toEnc : 변환 후 문자열의 인코딩 - 'alpha', 'ascii', 'bin', 'oct', 'hex' 

    이 함수는 string 으로부터 또다른 string 을 리턴해준다.
    """ 
    myList = string.split(' ')
    """
    
    myList 는 string 이 alpha가 아닌 경우에 필요하다. 
    you are great 와 같은 알파벳 문장은 스페이스 바까지 인코딩 대상에 해당한다. 
    하지만 ascii, bin, oct, hex는 그렇지 않다. 
    예를 들어 84 105 109 101 32 105 115 32 108 105 107 101 32 97 110 32 97 114 114 111 119 46 와 같이 
    아스키 코드로 인코딩 된 문장에서 스페이스 바는 그냥 숫자를 구분하는 역할을 할 뿐, 인코딩 대상이 아니다. 
    그래서 일이 복잡해진다...ㅠㅠ
    
    """ 
    if fromEnc == 'alpha':
        if toEnc == 'ascii':
            decoded = ' '.join(str(ord(char)) for char in string)
        elif toEnc == 'bin':
            decoded = ' '.join(str(format( ord(char), '#b')) for char in string)
        elif toEnc == 'oct':
            decoded = ' '.join(str(format( ord(char), '#o')) for char in string)
        elif toEnc == 'hex':
            decoded = ' '.join(str(format( ord(char), '#x')) for char in string)
        
    
    elif fromEnc == 'ascii': 
        if toEnc == 'alpha':
            decoded = ''.join(chr(int(num)) for num in myList)
        elif toEnc == 'bin':
            decoded = ' '.join(str(bin(int(num))) for num in myList)
        elif toEnc == 'oct':
            decoded = ' '.join(str(oct(int(num))) for num in myList)
        elif toEnc == 'hex':
            decoded = ' '.join(str(hex(int(num))) for num in myList)

    elif fromEnc == 'bin':
        if toEnc == 'alpha':
            decoded = ''.join(chr(int(num, 2)) for num in myList)
        elif toEnc == 'ascii':
            decoded = ' '.join(str(int(num, 2)) for num in myList)
        elif toEnc == 'oct':
            decoded = ' '.join(str(oct((int(num, 2)))) for num in myList)
        elif toEnc == 'hex':
            decoded = ' '.join(str(hex(int(num, 2))) for num in myList)
    
    elif fromEnc == 'oct':
        if toEnc == 'alpha': 
            decoded = ''.join(chr(int(num, 8)) for num in myList)
        elif toEnc == 'ascii':
            decoded = ' '.join(str(int(num, 8)) for num in myList)
        elif toEnc == 'bin':
            decoded = ' '.join(str(bin(int(num, 8))) for num in myList)
        elif toEnc == 'hex':
            decoded = ' '.join(str(hex(int(num, 8))) for num in myList)

    elif fromEnc == 'hex':
        if toEnc == 'alpha':
            decoded = ''.join(chr(int(num, 16)) for num in myList)
        elif toEnc == 'ascii':
            decoded = ' '.join(str(int(num, 16)) for num in myList)
        elif toEnc == 'bin':
            decoded = ' '.join(str(bin(int(num, 16))) for num in myList)
        elif toEnc == 'oct':
            decoded = ' '.join(str(oct(int(num, 16))) for num in myList)
    
    return decoded


sentence = input("Please enter sentence/word here: ")
fE = input("\nWhat type is your sentence? Choose from alpha, ascii, bin, oct, hex : ")


while True:
    tE = input("\nTo what type do you want to change your sentence? Choose from alpha, ascii, bin, oct, hex : ")
    encoded = convert(sentence,fE,tE)
    print("\nHere is your encoded text...\n")
    print(encoded+"\n")
    endOrContinue = input("Would you like to continue? Y/N: ")

    if endOrContinue == 'Y' or endOrContinue == 'y':
        fE = tE
        sentence = encoded

    elif endOrContinue == 'N' or endOrContinue == 'n':
        break
