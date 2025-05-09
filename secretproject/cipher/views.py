# cipher/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bosh sahifa")

def sezar(request):
    return HttpResponse("Sezar shifri")

def vejiner(request):
    return HttpResponse("Vejiner shifri")

def hill(request):
    return HttpResponse("Hill shifri")

def index(request):
    return HttpResponse("Index sahifasi")
def about_algorithms(request):
    return render(request, 'cipher/about_algorithms.html')

def caesar_view(request):
    return render(request, 'cipher/sezor1.html')

def vigenere_view(request):
    return render(request, 'cipher/vejiner1.html')

def hill_algorithm_detail(request):
    return render(request, 'cipher/hill1.html')
    
def affine_view(request):
    return render(request, 'cipher/affin1.html')

def about_algorithms_view(request):
    return render(request, 'about_algorithms.html')

# cipher/views.py

from django.shortcuts import render

# Bosh sahifa
def home(request):
    return render(request, 'cipher/index.html')  # Bu index.html sahifasini render qiladi

# Sezar shifrlash funksiyasi
def sezar_encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():  # Agar harf bo'lsa
            shift = key % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char  # Tinish belgisi yoki probelni o'zgartirmasdan qo'shamiz
    return result

# Deshifrlash
def sezar_decrypt(text, key):
    return sezar_encrypt(text, -key)  # Shunchaki kalitni teskari qo'shamiz

# Simulyatsiya funksiyasi
def sezar_simulate(text, key, action):
    simulation = ""
    for char in text:
        if char.isalpha():  # Agar harf bo'lsa
            shift = key % 26
            if action == 'encrypt':  # Shifrlash
                if char.islower():
                    new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
                elif char.isupper():
                    new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                simulation += f"{char} + {shift} → {new_char}\n"
            elif action == 'decrypt':  # Deshifrlash
                if char.islower():
                    new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                elif char.isupper():
                    new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                simulation += f"{char} - {shift} → {new_char}\n"
        else:
            simulation += f"{char} (o'zgarmaydi)\n"  # Tinish belgisi yoki probelni o'zgarmaydi
    return simulation

# Sezar shifrlash view funksiyasi
def sezar(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        key = int(request.POST.get('key', 0))
        action = request.POST.get('action')

        if action == 'encrypt':
            result = sezar_encrypt(text, key)
        elif action == 'decrypt':
            result = sezar_decrypt(text, key)
        elif action == 'simulate':
            result = sezar_simulate(text, key, action)
        
        return render(request, 'cipher/sezar.html', {'result': result, 'text': text, 'key': key, 'action': action})
    return render(request, 'cipher/sezar.html')

# cipher/views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def vejiner(request):
    text = request.POST.get('text', '') if request.method == 'POST' else ''
    key  = request.POST.get('key', '') if request.method == 'POST' else ''
    action = request.POST.get('action', 'encrypt') if request.method == 'POST' else 'encrypt'
    result = ''

    if request.method == 'POST':
        if not text:
            result = 'Iltimos, matn kiriting.'
        elif not key.isalpha():
            result = 'Kalit so‘z faqat lotin harflaridan iborat bo‘lishi kerak.'
        else:
            result = _vigenere_cipher(text, key, action)

    return render(request, 'cipher/vejiner.html', {
        'text': text,
        'key': key,
        'action': action,
        'result': result,
    })

# Yordamchi funksiya
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def vigenere_simulation(request):
    """
    View for Vigenère encryption/decryption with server-side result.
    Handles GET (show form) and POST (compute result).
    """
    text = ''
    key = ''
    action = 'encrypt'
    result = ''

    if request.method == 'POST':
        # Получаем данные из формы
        text = request.POST.get('text', '').strip()
        key = request.POST.get('key', '').strip()
        action = request.POST.get('action', 'encrypt')

        # Валидация
        if not text:
            result = 'Iltimos, matn kiriting.'
        elif not key.isalpha():
            result = 'Kalit so‘z faqat lotin harflaridan iborat bo‘lishi kerak.'
        else:
            result = _vigenere_cipher(text, key, action)

    return render(request, 'vejiner.html', {
        'text': text,
        'key': key,
        'action': action,
        'result': result,
    })


def _vigenere_cipher(text: str, key: str, action: str) -> str:
    """
    Applies Vigenère cipher to `text` using `key`.
    `action` can be 'encrypt' or 'decrypt'.
    Non-letter characters are preserved.
    """
    result_chars = []
    key = key.lower()
    key_index = 0
    key_len = len(key)

    for char in text:
        if char.isalpha():
            # Determine ASCII base
            base = ord('A') if char.isupper() else ord('a')
            # Current key character shift
            shift = ord(key[key_index % key_len]) - ord('a')
            code = ord(char) - base

            if action == 'encrypt':
                code = (code + shift) % 26
            else:
                code = (code - shift + 26) % 26

            result_chars.append(chr(code + base))
            key_index += 1
        else:
            # Preserve other characters
            result_chars.append(char)

    return ''.join(result_chars)

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def hill(request):
    """
    Hill shifrlash/simulyatsiya sahifasini ko'rsatadi.
    Barcha hisob-kitob va animatsiya JS tomonida amalga oshiriladi.
    """
    return render(request, 'cipher/hill_simulation.html')

from django.shortcuts import render
from .affine_cipher import affine_encrypt, affine_decrypt  # Affine Cipherni import qilish
def affine_cipher(request):
    return render(request, 'cipher/affine_cipher.html')
def affine(request):
    result = None
    text = ""
    a = b = 1
    steps = []

    if request.method == "POST":
        text = request.POST.get("text", "")
        a = int(request.POST.get("a", 1))
        b = int(request.POST.get("b", 0))
        action = request.POST.get("action")

        if action == "encrypt":
            result = affine_encrypt(text, a, b)

        elif action == "decrypt":
            result = affine_decrypt(text, a, b)

        elif action == "simulate":
            steps = []
            for char in text.upper():
                if char.isalpha():
                    x = ord(char) - ord('A')
                    y = (a * x + b) % 26
                    cipher_char = chr(y + ord('A'))
                    steps.append((char, x, y, cipher_char))
            result = ''.join([step[3] for step in steps])

    return render(request, 'cipher/affine_cipher.html', {
        'result': result,
        'text': text,
        'a': a,
        'b': b,
        'steps': steps
    })

