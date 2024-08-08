
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user to specify the desired length of the password
password_length = int(input("Enter the desired length of the password: "))

# Generate the password
password = generate_password(password_length)

# Display the generated password
print("Generated Password:", password)
