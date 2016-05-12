def KSA(key):
    keylength = len(key) #key is  list
    S = range(256)

    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]  # swap

    return S


def PRGA(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # swap

        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key):
    S = KSA(key)
    return PRGA(S)


def ByteToHex(byteStr):
    return ''.join(["%02X " % ord(x) for x in byteStr]).strip()



if __name__ == '__main__':

   
    key = 'NetStag'
    plaintext = str(raw_input("Enter the text to be encripted: "))
	
    def convert_key(s):
        return [ord(c) for c in s]
    
    key = convert_key(key)
    
    print(key)
	
    keystream = RC4(key)

    for c in plaintext:
            lst.append(chr(ord(c) ^ keystream.next()))
