import secrets
import hashlib
import bcrypt

salt = secrets.token_hex(16)  # Generate a random salt of 16 bytes (32 hex characters)
print(f"Generated salt: {salt}")

choice = input("which algorithm do you want to use? (SHA-256, SHA-512, Bcrypt): ")

if choice == "SHA-256":
    password = input("Enter a password: ")
    salted_password = password + salt  # Concatenate the password and salt
    hash_value = hashlib.sha256(salted_password.encode()).hexdigest()  # Hash the salted password using SHA-256
    print(f"Salted and hashed password: {hash_value}")

elif choice == "SHA-512":
    password = input("Enter a password: ")
    salted_password = password + salt  # Concatenate the password and salt
    hash_value = hashlib.sha512(salted_password.encode()).hexdigest()  # Hash the salted password using SHA-512
    print(f"Salted and hashed password: {hash_value}")

elif choice == "Bcrypt":
    password = input("Enter a password: ")
    salted_password = (password + salt).encode()  # Concatenate the password and salt, then encode to bytes
    hash_value = bcrypt.hashpw(salted_password, bcrypt.gensalt())  # Hash the salted password using Bcrypt
    print(f"Salted and hashed password: {hash_value.decode()}")  # Decode the hash to a string for display

else:
    print("Invalid choice. Please choose either SHA-256, SHA-512, or Bcrypt.")