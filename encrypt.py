from cryptography.fernet import Fernet

key = Fernet.generate_key()

crypter = Fernet(key)

password = crypter.encrypt(b"mypassword")
decrypt_password = crypter.decrypt(password)

print(str(password, 'utf8'))
print(str(decrypt_password, 'utf8'))

