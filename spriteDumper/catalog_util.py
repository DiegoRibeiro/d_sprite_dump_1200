import json

def load(path):
    print(path)
    with open(path + '\\catalog-content.json', "r") as f:
        data = bytearray(f.read(), 'utf8')
        catalog = json.loads(data)
        return catalog