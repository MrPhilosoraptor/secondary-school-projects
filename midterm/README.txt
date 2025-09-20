First, the appropriate libraries are imported for the program to work

String hash is declared, this encodes the given string to utf-8 before hashing it with the hash256 object. Finally it returns the digest from the object.
File hash is declared, this creates the hash256 object before reading the contents of the given file while encoding the contents to utf-8. It finally returns the digest from the hash object.
Encryption is declared, this takes a given string before encrypting it with the given cipher and returning the encrypted text.
Decryption is declared, this takes a given string before decoding it and then decrypting by using the given cipher. It then returns the decrypted text.
Write to file is declared, this takes a given series of characters and writes them to a file named "hashed_file.txt" and returns nothing.

Main is declared, this is where the Fernet key is generated a goes through a Fernet() function to be assigned to cipher_suite.

An if else statement checks whether the user is inputting a file or string.
If the user chooses file, it takes the name of the file and hashes it before encrypting the hash as well.
An if else statement checks if the decrpyted version of the hash and the normal hash still match, proving its integrity.
If it fails, it simply prints a message that something may have went wrong. Proper error handling has yet to be implemented.

If the user entered string, it starts by retrieving a string from the user.
It hashes the string before encrypting it.
An if statement checks if the decrypted hash matches the normal hash of the text. 
If it matches then it prints a success message before printing the encrypted hash.
Finally, if what the user chose matches nothing then it will tell them to print a valid option before the program stops.