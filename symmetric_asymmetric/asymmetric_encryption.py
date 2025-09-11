from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP



key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

message = str(input("Enter your message: "))
bytes_message = message.encode("utf-8")

cipher_rsa = PKCS1_OAEP.new(RSA.import_key(public_key))
cipher_text = cipher_rsa.encrypt(bytes_message)
print(public_key)
print(private_key)
print(f"\nEncrypted: {cipher_text}")


cipher_rsa = PKCS1_OAEP.new(RSA.import_key(private_key))
plain_text = cipher_rsa.decrypt(cipher_text)
print(f"\nDecrypted: {plain_text.decode()}")