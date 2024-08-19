def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'd':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            new_char = chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
            result += new_char
        else:
            result += char

    return result

text = input("Enter your message: ")
shift = int(input("Enter the shift value: "))
mode = input("Choose mode - (e)ncrypt or (d)ecrypt: ").lower()

result = caesar_cipher(text, shift, mode)
print("Result:", result)
