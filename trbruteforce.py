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
    parser.add_argument('-o', '--output', help='name of the output text file')
    parser.add_argument('-s', '--silent', help='do not display failed attempts', action='store_true')
    parser.add_argument('-n', '--non-interactive', help='do not ask for user input', action='store_true')
    args = parser.parse_args()


    # Output file
    if args.output is not None:
        out_file = open(args.output, "w")

    # Handle command line or file logic
    if args.input is not None:
        ct_file = open(args.input, "r")
        for line in ct_file:
            brute_force_transpose(line[:-1], args.silent, out_file if args.output else None, args.non_interactive)
    else:
        brute_force_transpose(args.ciphertext, args.silent, out_file if args.output else None, args.non_interactive)

def brute_force_transpose(ct,silent = False, outfile = None, nointeract = False):
    """
    Attempt to break the ciphertext by performing transposition decryption cipher from length 1 to ciphertext length.
    Check at each iteration the human readability threshold.
    If threshold is met, prompt user verification.

    ct - the ciphertext
    silent - flag to only display matches
    outfile - output to file
    nointeract - do not ask for user input
    """

    foundmatch = False

    for i in range(1, len(ct)+1):
        decrypted = decryptMessage(i, ct)
        flag = FindWord(decrypted)

        if flag is None and silent is False:
            output_fp("Failed to find: {}".format(decrypted), outfile, True)
        elif flag is not None:
            if nointeract is True:
                uinput = 'y'
            else:
                output_fp("Found word: {}".format(decrypted))
                uinput = (input("Is this the correct plaintext? [y/n]: ")).lower()
            if (uinput != "" and uinput[0] == 'y'):
                foundmatch = True
                output_fp("Found word: {}".format(decrypted),outfile)
                output_fp("Key size: {}".format(i), outfile)
                if nointeract is False:
                    return
    output_fp("", outfile)
    if foundmatch is False:
        output_fp("No match found for: \"{}\"\n".format(ct), outfile, False if silent is True else True)

def output_fp(msg, ofile = None, fp_out = False):
    """
    Print to standard out or to file.

    msg - the messsage to output
    ofile - file to output
    fp_out - output to both
    """
    if ofile is None:
        print(msg)
    else:
        ofile.write(msg + "\n")
        if fp_out is True:
            print(msg)
    return

if __name__ == "__main__":
    main()
