## kriftografi Substitution Ciphers
def create_substitution_cipher(key):
    """
    Membuat tabel substitusi berdasarkan kunci.
    
    Parameters:
    key (str): Kunci substitusi yang harus berisi semua huruf alfabet tanpa duplikasi dan panjangnya 26 huruf.
    
    Returns:
    dict: Kamus yang memetakan setiap huruf alfabet ke huruf sesuai dengan kunci.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if len(key) != 26 or len(set(key)) != 26 or not key.isalpha():
        raise ValueError("Kunci harus panjang 26 huruf dan berisi semua huruf alfabet tanpa duplikasi.")
    
    substitution_dict = dict(zip(alphabet, key))
    return substitution_dict

def encrypt(message, substitution_dict):
    """
    Mengenkripsi pesan menggunakan tabel substitusi.
    
    Parameters:
    message (str): Pesan yang akan dienkripsi.
    substitution_dict (dict): Kamus substitusi yang memetakan huruf asli ke huruf yang dienkripsi.
    
    Returns:
    str: Pesan yang telah dienkripsi.
    """
    encrypted_message = ''
    for char in message:
        if char.lower() in substitution_dict:
            new_char = substitution_dict[char.lower()]
            if char.isupper():
                new_char = new_char.upper()
            encrypted_message += new_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(encrypted_message, substitution_dict):
    """
    Mendekripsi pesan menggunakan tabel substitusi.
    
    Parameters:
    encrypted_message (str): Pesan yang telah dienkripsi.
    substitution_dict (dict): Kamus substitusi yang memetakan huruf yang dienkripsi kembali ke huruf asli.
    
    Returns:
    str: Pesan yang telah didekripsi.
    """
    reverse_substitution_dict = {v: k for k, v in substitution_dict.items()}
    decrypted_message = ''
    for char in encrypted_message:
        if char.lower() in reverse_substitution_dict:
            new_char = reverse_substitution_dict[char.lower()]
            if char.isupper():
                new_char = new_char.upper()
            decrypted_message += new_char
        else:
            decrypted_message += char                                                                                                 
    return decrypted_message

# Contoh penggunaan
if __name__ == "__main__":
    # Definisikan kunci substitusi
    key = 'zyxwvutsrqponmlkjihgfedcba'  # Misalnya, kunci ini membalikkan alfabet

    # Buat tabel substitusi
    substitution_dict = create_substitution_cipher(key)

    # Pesan yang akan dienkripsi
    message = 'Hello, World!'

    # Enkripsi pesan
    encrypted = encrypt(message, substitution_dict)

    # Dekripsi pesan
    decrypted = decrypt(encrypted, substitution_dict)

    # Tampilkan hasil
    print(f'Original: {message}')
    print(f'Encrypted: {encrypted}')
    print(f'Decrypted: {decrypted}')
