from cryptography.fernet import Fernet
key = Fernet.generate_key()

with open('unlock.key', 'wb') as unlock:
     unlock.write(key)

f = Fernet(key)
# Encryption
with open('responses.txt', 'rb') as original_file:
     original = original_file.read()

encrypted = f.encrypt(original)

with open ('enc_responses.txt', 'wb') as encrypted_file:
     encrypted_file.write(encrypted)

# Decryption
with open('enc_responses.txt', 'rb') as encrypted_file:
     encrypted = encrypted_file.read()

decrypted = f.decrypt(encrypted)

with open('dec_responses.txt', 'wb') as decrypted_file:
     decrypted_file.write(decrypted)

