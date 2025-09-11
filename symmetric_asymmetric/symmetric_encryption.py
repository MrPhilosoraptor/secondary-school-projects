from cryptography.fernet import Fernet


key = Fernet.generate_key()
cipher_suite = Fernet(key)


message = str(input("Enter your message: "))
bytes_message = message.encode("utf-8")

cipher_text = cipher_suite.encrypt(bytes_message)
print(key)
print(f"Encrypted: {cipher_text}")


plain_text = cipher_suite.decrypt(cipher_text)
print(f"Decrypted: {plain_text.decode()}")