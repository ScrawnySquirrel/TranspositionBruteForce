#!/usr/bin/python3.7

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
    # TODO: Implement output to file
    parser.add_argument('-o', '--output', help='name of the output text file')
    parser.add_argument('-s', '--silent', help='do not display failed attempts', action='store_true')
    args = parser.parse_args()

    # Handle command line or file logic
    if args.input is not None:
        ct_file = open(args.input, "r")
        for line in ct_file:
            brute_force_transpose(line[:-1], args.silent)
    else:
        brute_force_transpose(args.ciphertext, args.silent)

def brute_force_transpose(ct,silent = False):
    """
    Attempt to break the ciphertext by performing transposition decryption cipher from length 1 to ciphertext length.
    Check at each iteration the human readability threshold.
    If threshold is met, prompt user verification.

    ct - the ciphertext
    silent - flag to only display matches
    """
    for i in range(1, len(ct)+1):
        decrypted = decryptMessage(i, ct)
        flag = FindWord(decrypted)

        if flag is None and silent is False:
            print('Failed to find: %s' % (decrypted))
        elif flag is not None:
            print('Found word: ', decrypted)
            uinput = (input("Is this the correct plaintext? [y/n]: ")).lower()
            if (uinput != "" and uinput[0] == 'y'):
                print("Key size: {}".format(i))
                return
    input("No match found for: \"{}\"".format(ct))

if __name__ == "__main__":
    main()
