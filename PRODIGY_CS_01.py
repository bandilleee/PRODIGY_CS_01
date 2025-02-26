def caesar_cipher(text, shift_value, operation_mode):
    result = ""

    for char in text:
        if char.isalpha():  # Checking if the character is a letter
            shift_amount = shift_value if operation_mode == 'encrypt' \
                else -shift_value

            # This is to determine if it's uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')

            # Performing the shift
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char

    return result


mode = input("Hi there! Would you like to encrypt or decrypt? ").strip().lower()
message = input("Please enter your message: ")
shift = int(input("Please enter a shift value: "))

# This is to perform encryption or decryption
if mode in ['encrypt', 'decrypt']:
    output = caesar_cipher(message, shift, mode)
    print(f"Results successfully converted: {output}")
else:
    print("That's an Invalid mode! Please enter 'encrypt' or 'decrypt'.")
