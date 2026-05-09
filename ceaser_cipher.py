"""
Caesar Cipher - Encryption and Decryption Program
Allows users to encrypt and decrypt text using a shift value
"""

def caesar_encrypt(text, shift):
    """
    Encrypts text using Caesar Cipher
    
    Args:
        text (str): The text to encrypt
        shift (int): The shift value (1-25)
    
    Returns:
        str: Encrypted text
    """
    result = ""
    
    for char in text:
        if char.isalpha():
            # Check if uppercase or lowercase
            if char.isupper():
                # Shift uppercase letters
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Shift lowercase letters
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result


def caesar_decrypt(text, shift):
    """
    Decrypts text using Caesar Cipher
    
    Args:
        text (str): The text to decrypt
        shift (int): The shift value used for encryption
    
    Returns:
        str: Decrypted text
    """
    # Decryption is just encryption with negative shift
    return caesar_encrypt(text, -shift)


def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("Caesar Cipher - Encryption & Decryption")
    print("="*50)
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Brute force decryption (try all shifts)")
    print("4. Exit")
    print("="*50)


def brute_force_decrypt(text):
    """
    Tries all possible shifts to decrypt the text
    
    Args:
        text (str): The encrypted text
    
    Returns:
        None (prints all possible decryptions)
    """
    print("\nBrute force decryption (all possible shifts):")
    print("-" * 50)
    for shift in range(26):
        decrypted = caesar_decrypt(text, shift)
        print(f"Shift {shift:2d}: {decrypted}")
    print("-" * 50)


def main():
    """Main program loop"""
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Encryption
            message = input("\nEnter the message to encrypt: ")
            while True:
                try:
                    shift = int(input("Enter the shift value (0-25): "))
                    if 0 <= shift <= 25:
                        break
                    else:
                        print("Please enter a value between 0 and 25")
                except ValueError:
                    print("Please enter a valid number")
            
            encrypted = caesar_encrypt(message, shift)
            print(f"\nOriginal message: {message}")
            print(f"Shift value: {shift}")
            print(f"Encrypted message: {encrypted}")
        
        elif choice == '2':
            # Decryption
            message = input("\nEnter the message to decrypt: ")
            while True:
                try:
                    shift = int(input("Enter the shift value that was used for encryption (0-25): "))
                    if 0 <= shift <= 25:
                        break
                    else:
                        print("Please enter a value between 0 and 25")
                except ValueError:
                    print("Please enter a valid number")
            
            decrypted = caesar_decrypt(message, shift)
            print(f"\nEncrypted message: {message}")
            print(f"Shift value: {shift}")
            print(f"Decrypted message: {decrypted}")
        
        elif choice == '3':
            # Brute force
            message = input("\nEnter the encrypted message: ")
            brute_force_decrypt(message)
        
        elif choice == '4':
            print("\nThank you for using Caesar Cipher. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
