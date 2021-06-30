#python3.6
from struct import unpack
import sys

filename = sys.argv[1]
zero = b'\x00'

with open(filename[:4] + ".txt", 'wb') as fo:
    with open(filename, 'rb') as f:
        fLen = len(f.read())-1
        f.seek(4)
        fo.write(f"{str(unpack('i', f.read(4))[0])}\r\n".encode()) #display interval
        print(f"fLne {str(fLen)} | fSeek {str(f.tell())}")
        while f.tell() < fLen:
            first = unpack("i", f.read(4))[0] #starting timing for subtitle
            second = unpack("i", f.read(4))[0] + first #ending timing for subtitle
            lineLength = unpack("i", f.read(4))[0] #length of current subtitle text
            fo.write(f"{str(first)}, {str(second)}, {f.read(lineLength).rstrip(zero).decode()}\r\n".encode()) #write line to file
            print(f"F {str(first)} S {str(second)} LL {str(lineLength)}")
            f.read(8)
