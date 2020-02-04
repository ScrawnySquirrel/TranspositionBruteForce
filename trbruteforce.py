#!/usr/bin/python3.5

import argparse

from trencode import *
from trdecode import *
from detectEnglish import *
from testlang import *

# Define script description and the arugment list
parser = argparse.ArgumentParser(description='Attempt to brute force the transposition cipher.')
parser.add_argument('-c', '--ciphertext', help='the ciphertext to decode', required=True)
parser.add_argument('-i', '--input', help='name of the input text file')
parser.add_argument('-o', '--output', help='name of the output text file')
args = parser.parse_args()

for i in range(1, len(args.ciphertext)+1):
    # print(i)
    decrypted = decryptMessage(i, args.ciphertext)
    flag = FindWord(decrypted)

    if flag == None:
        print('Failed to find: %s' % (decrypted))
    else:
        print('Found word: ', decrypted)
        uinput = (input("Is this the correct plaintext? [y/n]: ")).lower()
        if (uinput != "" and uinput[0] == 'y'):
            print("neato")
            exit()
