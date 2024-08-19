from PIL import Image
import numpy as np
import os

def encrypt_image(input_path, output_path, key):
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"The file {input_path} does not exist.")
    img = Image.open(input_path) #Using open() to use the pic
    img_array = np.array(img)
    encrypted_array = img_array ^ key
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"The file {input_path} does not exist.")
    img = Image.open(input_path)
    img_array = np.array(img)
    decrypted_array = img_array ^ key
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    print("Image Encryption/Decryption Tool")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        input_image_path = input("Enter the path of the image to encrypt :")
        encrypted_image_path = input("Enter the path to save the encrypted image : ")
        key = int(input("Enter an integer key for encryption: "))
        encrypt_image(input_image_path, encrypted_image_path, key)
    elif choice == '2':
        input_image_path = input("Enter the path of the image to decrypt : ")
        decrypted_image_path = input("Enter the path to save the decrypted image : ")
        key = int(input("Enter an integer key for decryption: "))
        decrypt_image(input_image_path, decrypted_image_path, key)
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
