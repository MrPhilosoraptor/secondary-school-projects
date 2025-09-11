The symmetric encryption file works via the functions of Fernet from the cryptography library for Python
Firstly a key is generated and then a cipher is created with the Fernet() functions
A message is then retrieved from the user before being converted to a byte literal in utf-8 encoding
The message is then finally encrypted with the .encrypt call before the key is printed out as well as the encrypted message
Lastly, the message is decrypted with the .decrypt function before the decrypted message is printed out

The asymmetric encryption first imports the RSA and PKCS1_OAEP padding scheme to be used for RSA encryption
A key is created with 2,048 random consecutive bytes using the RSA.generate() before a private and public key is derived from that original key
A message is retrieved and encoded again
A new encryption object is created with the public key using PKCS1_OAEP as well, this is then used to encrypt the message
After the keys and encrypted message are printed, the message is then decrypted with the PKCS1_OAEP object, this time using the private key
The decrypted message is finally printed