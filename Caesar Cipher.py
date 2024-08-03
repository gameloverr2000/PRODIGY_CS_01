def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    choice = input("(E)ncrypt or (D)ecrypt: ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' or 'D'.")
        return

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (1-25): "))

    if choice == 'E':
        result = caesar_encrypt(text, shift)
        print(f"Encrypted text: {result}")
    else:
        result = caesar_decrypt(text, shift)
        print(f"Decrypted text: {result}")

if __name__ == "__main__":
    main()