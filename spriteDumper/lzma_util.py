import lzma

def decompress(name, data):
    out = lzma.decompress(data, lzma.FORMAT_AUTO, None)
    with open(name, "wb") as orig:
        orig.write(out)

def fix_header(filepath):
    with open(filepath, 'rb') as f:
        data = bytearray(f.read())
        data = data[32:]
        data[5] = 255
        data[6] = 255
        data[7] = 255
        data[8] = 255
        data[9] = 255
        data[10] = 255
        data[11] = 255
        data[12] = 255
        return data



    
    
    
        