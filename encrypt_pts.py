import argparse
import trencode as tre

parser = argparse.ArgumentParser(description='continuous encrypt plaintexts using transpose cipher.')
parser.add_argument('-o', '--output', help='name of the output text file', required=True)
args = parser.parse_args()

out_f = open(args.output, "a+")

while 1:
    plaintext = input("Plaintext: ")
    if plaintext is "":
        exit()
    key = input("Key: ")
    if key is "" or key.isnumeric() is False:
        print("Key must be numeric.")
        exit()
    ciphertext = tre.encryptMessage(int(key), plaintext)
    print("Ciphertext: {}".format(ciphertext))
    out_f.write("{}\n".format(ciphertext))
