#!/usr/bin/python3.5

import argparse

from trencode import *
from trdecode import *
from detectEnglish import *
from testlang import *

def main():
    # Define script description and the arugment list
    parser = argparse.ArgumentParser(description='Attempt to brute force the transposition cipher.')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-c', '--ciphertext', help='the ciphertext to decode')
    group.add_argument('-i', '--input', help='name of the input text file')
    parser.add_argument('-o', '--output', help='name of the output text file')
    args = parser.parse_args()

    if args.input is not None:
        ct_file = open(args.input, "r")
        for line in ct_file:
            brute_force_transpose(line[:-1])
    else:
        brute_force_transpose(args.ciphertext)

def brute_force_transpose(ct):
    for i in range(1, len(ct)+1):
        print(i)
        decrypted = decryptMessage(i, ct)
        flag = FindWord(decrypted)

        if flag == None:
            print('Failed to find: %s' % (decrypted))
        else:
            print('Found word: ', decrypted)
            uinput = (input("Is this the correct plaintext? [y/n]: ")).lower()
            if (uinput != "" and uinput[0] == 'y'):
                print("neato")
                return
    input("No match found for: \"{}\"".format(ct))

if __name__ == "__main__":
    main()
