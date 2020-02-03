#!/usr/bin/python3.4

# Test the language detecion library

import detectEnglish, sys, getopt

def main (argv):
    try:
        opts, args = getopt.getopt (argv, "t:",["ptext="])
    
    except getopt.getoptError:
        sys.exit (1)
    
    if len (sys.argv[1:]) < 2:
        print ('Usage: ./testlang.py -t <word>')
        sys.exit(1)
    for opt, arg in opts:
        if opt in opt in ("-t", "--ptext"):
            plaintext = arg
                
    # Check the dictionary
    flag = FindWord (plaintext)
    
    if flag == None:
        print('Failed to find: %s' % (plaintext))
    else:
        print('Found word: ', plaintext)
    
def FindWord (plaintext):
    if detectEnglish.FindEnglish(plaintext):
        return True
    
    return None
        
    
# the main() function.
if __name__ == "__main__":
    main (sys.argv[1:])
