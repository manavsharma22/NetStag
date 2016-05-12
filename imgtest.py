import os
import io
import Image
from array import array

def readimage(path):
    count = os.stat(path).st_size / 2
    with open(path, "rb") as f:
        return bytearray(f.read())

bytes = readimage("test.png")
#return bytes
with open("testme.txt","wb") as f:
	f.write(bytes)

#image = Image.open(io.BytesIO(bytes))
#image.save("testresult.jpg")
