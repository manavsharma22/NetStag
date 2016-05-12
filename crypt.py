import rc4

def ByteToHex(byteStr):
    return ''.join(["%02X" % ord(x) for x in byteStr]).strip()

def crypt(data):
    key = 'NetStag'
    cryptlist = []

    def convert_key(key):
        return [ord(c) for c in key]

    key = convert_key(key)
    #print(key)
    keystream = rc4.RC4(key)
    """
    import sys
    for c in data:
        sys.stdout.write("%02X" % (ord(c) ^ keystream.next()))
    print
    """
    for c in data:
        cryptlist.append(chr((ord(c) ^ keystream.next())))

    ans = ByteToHex("".join(cryptlist))
    return ans

if __name__ == "__main__":

    with open('test.txt','rb') as f:

        read_bytes='xOn'
        key = 'NetStag'
        offset=10
        x=1
        y=2
        b='None'
        c='None'
        lst=[]


        while read_bytes!='':
            read_bytes=f.read(offset)
            lst.append(read_bytes)
            if y>x:
                f.seek(offset,0)
                y=y-x

    lst2 = []
    for plaintext in lst:
        lst2.append(crypt(plaintext))

    ans = "\n".join(lst2)
    print ans
