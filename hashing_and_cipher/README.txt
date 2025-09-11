The caesar cipher program first imports random to generate the amount the letters will be shifted by
It also retrieves the input string that will be encrypted before initializing an empty string that will be used to create the encrypted string
It starts the for loop and first checks if the current character in the input string is alphabetical
It then checks if the character is alphabetical, but if the character is a space it will immediately add it to the end string
After passing the first check, it shifts it positively by the shift number before checking if the result is still a letter
If it is not a letter, it will shift the letter negatively instead before moving on
It then changes the character number back to a letter with the chr() function before adding the letter to the string
It finally prints the encrypted string and the shift number used for the string


The hash 256 program starts by importing the hashlib that makes this program possible
It starts by initializing two functions, one for handling strings and the other for files
The string hash function takes a string and converts it to bytes before creating a sha256 object
The sha256 object is then used with the bytes literal to update the object before returning the digest of the string
The file hash function takes a file name and then creates an sha256 object 
It then opens the file given by the user and reads the file's contents before converting the read contents to bytes with the .encode() function
After reading the file, it creates a new file and writes the contents of the updated sha256 object to the file

After the functions are declared, the program takes a string from the user
This string is used to decide whether it will run the string or file functions
If it does the string function, it takes a string to be hashed before passing it to the function and printing the results
If it does the file function, it takes a string to be used as the file name before passing it to the file function
The file option also handles an error, telling the user that a hashed file already exists if it returns an error when trying to run the function
If the user's selected option is not file or string, it tells them to pick a valid option before ending