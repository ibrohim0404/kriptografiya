# Affine Cipher uchun yordamchi funktsiyalar

# a ning mod 26 bo'yicha teskari qiymatini hisoblash
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Affine shifrlash funktsiyasi
def affine_encrypt(text, a, b):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Faqat harflarni shifrlash
            x = ord(char.upper()) - ord('A')  # Harfni indeksga aylantirish
            encrypted_char = chr((a * x + b) % 26 + ord('A'))  # Shifrlash formulasi
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Agar belgilar bo'lsa, ularni saqlash
    return encrypted_text

# Affine deshifrlash funktsiyasi
def affine_decrypt(text, a, b):
    decrypted_text = ""
    a_inv = mod_inverse(a, 26)  # a ning mod 26 bo'yicha teskari qiymati
    if a_inv is None:
        return "Invalid key, no modular inverse"
    
    for char in text:
        if char.isalpha():
            x = ord(char.upper()) - ord('A')
            decrypted_char = chr((a_inv * (x - b)) % 26 + ord('A'))  # Deshifrlash formulasi
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Agar belgilar bo'lsa, ularni saqlash
    return decrypted_text
