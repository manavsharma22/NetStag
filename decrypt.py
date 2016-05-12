import rc4

def HexToByte( hexStr ):

    bytes = []
    #hexStr = ''.join( hexStr.split() )

    for i in range(0, len(hexStr), 2):
        bytes.append( chr( int (hexStr[i:i+2], 16 ) ) )
    return ''.join( bytes )

def decrypt(data):
    key = 'NetStag'
    decryptlist = []
    data = HexToByte(data)
    def convert_key(key):
        return [ord(c) for c in key]

    key = convert_key(key)
    keystream = rc4.RC4(key)

    for c in data:
            decryptlist.append(chr(ord(c) ^ keystream.next()))

    ans = "".join(decryptlist)
    return ans


if __name__ == '__main__':

    key = 'NetStag'
    data = str(raw_input("Enter the data to decrypt: "))
    data = HexToByte(data)

    def convert_key(s):
        return [ord(c) for c in s]
    key = convert_key(key)

    keystream = rc4.RC4(key)
    lst = []
    for c in data:
            lst.append(chr(ord(c) ^ keystream.next()))

    #ans = ByteToHex("".join(lst))
    ans = "".join(lst)
    print ans
