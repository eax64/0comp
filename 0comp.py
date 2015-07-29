#!/usr/bin/env python3

import argparse
import base64
import zlib
import gzip
import bz2
import sys
import os

MAX_FILENAME_LEN = 255

def compress(fn, bigfn):
    data = open(fn, "rb").read()
    compressed = sorted([(base64.b64encode(bytes([i])+comp.compress(data))).decode("utf8").replace("/", "_") for i,comp in enumerate([bz2, gzip, zlib])], key=len)
    if len(compressed[0]) > MAX_FILENAME_LEN and not bigfn:
        exit("The compressed file is too big to be saved (%d>%d). Add --bigfile to allow bigfile compression." % (len(compressed[0]), MAX_FILENAME_LEN))
    if not bigfn:
        open(compressed[0], "w").close()
        print("The compressed file has been saved in the file: %s" % compressed[0])
    else:
        os.mkdir(bigfn)
        chunks = [compressed[0][i:i+MAX_FILENAME_LEN] for i in range(0, len(compressed[0]), MAX_FILENAME_LEN)]
        for i,f in enumerate(chunks):
            open("%s/%s" % (bigfn, f), "w").close()
            os.utime("%s/%s" % (bigfn, f), (i,i))
        print("The compressed file has been saved in the file: %s" % bigfn)

def decompress(fn):
    if not os.path.isdir(fn):
        data = base64.b64decode(fn.replace("_", "/").encode("utf8"))
    else:
        data = "".join(sorted(os.listdir(fn), key=lambda x: int(os.stat("%s/%s" % (fn, x)).st_mtime)))
        data = base64.b64decode(data.replace("_", "/").encode("utf8"))
    comptype, data = data[0], data[1:]
    sys.stdout.buffer.write([bz2, gzip, zlib][comptype].decompress(data))
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--compress", action="store_true", help="Compression mode")
    parser.add_argument("-d", "--decompress", action="store_true", help="Decompression mode")
    parser.add_argument("-b", "--bigfilename", help="Enable compression of bigfiles when you specify a filename")
    parser.add_argument('FILENAME', help="The file to (de)compress")
    args = parser.parse_args()

    if args.compress == args.decompress:
        exit("You must choose one option betwen -c and -d")

    if args.compress:
        compress(args.FILENAME, args.bigfilename)
    else:
        decompress(args.FILENAME)
