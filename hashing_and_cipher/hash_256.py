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
    with open("hashed_file.txt", "x") as new_file:
        new_file.write(f"The result of the hashing is: {hash256.digest()}")

def main(option):
    if option == "file":
        try:
            user_file = str(input("Enter your file in current directory: "))
            file_hash(user_file)
        except FileExistsError:
            print("A hashed file already exists. Please remove the current hashed file before making a new one.")
    elif option == "string":
        user_string = str(input("Enter your string:\n"))
        print(f"Here is the hashed string {string_hash(user_string)}")
    else:
        print("Please enter a valid option")

user_choice = str(input("Would you like to encrypt a file or string? ")).lower()

main(user_choice)