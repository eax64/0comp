#!/usr/bin/env python3

import argparse
import base64
import zlib
import gzip
import bz2
import sys

MAX_FILENAME_LEN = 255

def compress(fn):
    data = open(fn, "rb").read()
    compressed = sorted([(base64.b64encode(bytes([i])+comp.compress(data))).decode("utf8").replace("/", "_") for i,comp in enumerate([bz2, gzip, zlib])], key=len)
    if len(compressed[0]) > MAX_FILENAME_LEN:
        exit("The compressed file is too big to be saved. (%d>%d)" % (len(compressed[0]), MAX_FILENAME_LEN))
    open(compressed[0], "w").close()
    print("The compressed file has been saved in the file: %s" % compressed[0])

def decompress(fn):
    data = base64.b64decode(fn.replace("_", "/"))
    comptype, data = data[0], data[1:]
    sys.stdout.write([bz2, gzip, zlib][comptype].decompress(data).decode("utf8"))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--compress", action="store_true", help="Compression mode")
    parser.add_argument("-d", "--decompress", action="store_true", help="Decompression mode")
    parser.add_argument('FILENAME', help="The file to (de)compress")
    args = parser.parse_args()

    if args.compress == args.decompress:
        exit("You must choose one option betwen -c and -d")

    if args.compress:
        compress(args.FILENAME)
    else:
        decompress(args.FILENAME)
