# TranspositionBruteForce

Program to attempt breaking Transposition ciphers using brute force.
Iterate each key size until a certain threshold of human readable words have been found.

## Getting Started

These instruction will help break the given ciphertext encrypted using the Transposition cipher and display the plaintext/key combination.

## Prerequisite

* Python3

## Usage
### Arguments
* `-c, --ciphertext`
* `-i, --input`
* `-o, --output`
* `-s, --silent`
* `-n, --non-interactive`

> All the optional arguments (`-o`, `-s`, `-n`) maybe used used in conjunction with each other.

#### Inputting the Ciphertext
The program has 2 ways of taking in the ciphertext: command-line and text file.
It is required that the ciphertext is provided using either method for the program to execute properly.

##### Command-line Method
```
python3 -B trbruteforce.py -c <ciphertext>
```

##### Text File Method
```
python3 -B trbruteforce.py -i <ciphertextfile>
```
> Each ciphertext must be in its own line.

#### Output Results to File
The `-o` argument allows the output of the program to be saved to a text file.
```
python3 -B trbruteforce.py -c <ciphertext> -o <outputfile>
```

#### Display Matches Only
For longer ciphertexts, the output can be overwhelming as it iterates every key size and cover up the entire screen. The `-s` argument will only display possible matches.
```
python3 -B trbruteforce.py -c <ciphertext> -s
```

#### No User Prompt
Due to the nature of brute force, it can take a long time for the program to run through each possible key size and long ciphertexts. Instead of waiting long gaps between matches, the program can simply output without user intervention using `-n` argument.
```
python3 -B trbruteforce.py -c <ciphertext> -n
```

> In conjunction with the `-s` argument, the `-n` argument is extremely helpful for users to review all possible matches at once.

## Running the tests



## Author

**Gabriel Lee** - [ScrawnySquirrel](https://github.com/ScrawnySquirrel)
