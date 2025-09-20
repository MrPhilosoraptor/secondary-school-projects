from cryptography.fernet import Fernet
import hashlib

def string_hash(input_string):
    bytes_string = input_string.encode("utf-8")
    hash256 = hashlib.sha256()
    hash256.update(bytes_string)
    return hash256.digest()

def file_hash(file_to_hash):
    hash256 = hashlib.sha256()
    with open(file_to_hash, "r") as file:
        hash256.update(file.read().encode("utf-8"))
    return hash256.digest()

def encryption(user_input, cipher):
    cipher_text = cipher.encrypt(user_input)
    return cipher_text

def decryption(user_text, cipher):
    user_text.decode()
    plain_text = cipher.decrypt(user_text)
    return plain_text

def write_to_file(user_input):
    with open("hashed_file.txt", "x") as new_file:
        new_file.write(f"{user_input}")

def main(option):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    if option == "file":
        user_file = str(input("Enter your file in current directory: ")).strip()
        encryptedAndHashed = encryption(file_hash(user_file), cipher_suite)
        try:
            if decryption(encryptedAndHashed, cipher_suite) == file_hash(user_file):
                write_to_file(encryptedAndHashed)
                print("Successfully wrote the new contents to a new file. Check your directory.")
            else:
                print("Something seems to have went wrong.")
        except FileExistsError:
            print("A hashed file already exists in the current directory. Please remove this to create a new one.")

    elif option == "string":
        user_string = str(input("Enter your string:\n"))
        encryptedAndHashed = encryption(string_hash(user_string), cipher_suite)
        if decryption(encryptedAndHashed, cipher_suite) == string_hash(user_string):
            print("The text has been hashed and encrypted successfully. See below for the result.")
            print(encryptedAndHashed)
    else:
        print("Please enter a valid option")

user_choice = str(input("What type of input will you be using? ")).lower()

main(user_choice)