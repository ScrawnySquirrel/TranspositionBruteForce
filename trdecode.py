#!/usr/bin/python3.5

# Transposition Cipher Decryption

import math, sys, getopt

def main (argv):
    
    try:
        opts, args = getopt.getopt (argv, "ht:k:",["ctext=", "keysize="])
    
    except getopt.getoptError:
        sys.exit (1)
    
    if len (sys.argv[1:]) < 4:
        print ('Usage: ./trdecode.py -t <plaintext> -k <keysize>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Usage: ./trdecode.py -t <plaintext> -k <keysize>')
            sys.exit ()
        elif opt in ("-t", "--ctext"):
            ciphertext = arg
        elif opt in ("-k", "--keysize"):
            keylen = int (arg)
    
    # call the crypto function
    plaintext = decryptMessage (keylen, ciphertext)

    # Print the plaintext
    print(plaintext)

#--------------------------------------------------------------------------------------    

 # The transposition decrypt function will simulate the "columns" and
 # "rows" of the grid that the plaintext is written on by using a list
 # of strings. First, we need to calculate a few values.

def decryptMessage(key, message):
 
    # Determine the number of columns
    nCols = math.ceil (len (message) / key)
    
    # Determine the number of rows
    nRows = key
    
    # Determine the unused cells 
    nUnused = (nCols * nRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * nCols

    # row and col point to the location of the next character in the ciphertext
    row = col = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1 # point to next column

        # If it reaches the last column in the row, or at an unused cell, start processing the next row 
        if (col == nCols) or (col == nCols - 1 and row >= nRows - nUnused):
            col = 0
            row += 1

    return ''.join(plaintext)


# main() function
if __name__ == "__main__":
    main (sys.argv[1:])
