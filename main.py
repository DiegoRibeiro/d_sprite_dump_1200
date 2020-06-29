# -*- coding: utf-8 -*-
import sys
import os
import re
from spriteDumper import lzma_util
from spriteDumper import catalog_util
from pathlib import Path

def main(argv):
    assets_folder = argv[1]
    catalog = catalog_util.load(assets_folder)
    print(len(catalog))

    Path("output/sprites").mkdir(parents=True, exist_ok=True)

    for i in catalog:        
        if i['type'] == 'sprite':
            # pattern for name firstspriteid-lastspriteid-spritetype-area.bmp
            print(i)
            data = lzma_util.fix_header(assets_folder + "\\" + i['file'])
            lzma_util.decompress("output/sprites/" + str(i['firstspriteid']) + "-" + str(i['lastspriteid']) + "-" + str(i['spritetype']) + "-" + str(i['area']) + ".bmp", data)
        else:
            print(i)
    
    # there are files that are not in the catalog and it is compressed using lzma. The names are: subarea-*, satellite-*, minimap-*

    # for subarea-*
    files = [f for f in os.listdir(assets_folder) if re.match(r'subarea-.*', f)]
    Path("output/subarea").mkdir(parents=True, exist_ok=True)

    for i in files:
        print(i)
        data = lzma_util.fix_header(assets_folder + "\\" + i)
        lzma_util.decompress("output/subarea/" + os.path.splitext(i)[0], data)

    # for satellite-*
    files = [f for f in os.listdir(assets_folder) if re.match(r'satellite-.*', f)]
    Path("output/satellite").mkdir(parents=True, exist_ok=True)

    for i in files:
        print(i)
        data = lzma_util.fix_header(assets_folder + "\\" + i)
        lzma_util.decompress("output/satellite/" + os.path.splitext(i)[0], data)

    #for minimap-*
    files = [f for f in os.listdir(assets_folder) if re.match(r'minimap-.*', f)]
    Path("output/minimap").mkdir(parents=True, exist_ok=True)

    for i in files:
        print(i)
        data = lzma_util.fix_header(assets_folder + "\\" + i)
        lzma_util.decompress("output/minimap/" + os.path.splitext(i)[0], data)


if __name__ == "__main__":
    main(sys.argv)


