Load modules for transposition and language detection
Get ciphertext(s)
For each ciphertext
  Loop through key size 1 to length of ciphertext
    Decrypt using possible Key
      Check for detected English words
      Prompt user verification
      If yes
        break
  Output results to file
