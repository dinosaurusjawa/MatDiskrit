## kriftografi Transposition Ciphers
def encrypt_transposition_cipher(message, key):
    """
    Mengenkripsi pesan menggunakan Columnar Transposition Cipher.
    
    Parameters:
    message (str): Pesan yang akan dienkripsi.
    key (str): Kunci yang menentukan urutan kolom.
    
    Returns:
    str: Pesan yang telah dienkripsi.
    """
    # Remove spaces from the message
    message = message.replace(" ", "")
    
    # Determine the number of columns based on the length of the key
    num_cols = len(key)
    
    # Create a table to hold the characters
    table = [''] * num_cols
    for i in range(num_cols):
        table[i] = [''] * (len(message) // num_cols + 1)
    
    # Fill the table with characters from the message
    for i, char in enumerate(message):
        col = i % num_cols
        row = i // num_cols
        table[col][row] = char
    
    # Read the columns in order defined by the key
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    encrypted_message = ''.join(
        ''.join(table[col][row] for row in range(len(table[col])))
        for col in key_order
    )
    
    return encrypted_message

def decrypt_transposition_cipher(encrypted_message, key):
    """
    Mendekripsi pesan menggunakan Columnar Transposition Cipher.
    
    Parameters:
    encrypted_message (str): Pesan yang telah dienkripsi.
    key (str): Kunci yang menentukan urutan kolom.
    
    Returns:
    str: Pesan yang telah didekripsi.
    """
    num_cols = len(key)
    num_rows = len(encrypted_message) // num_cols
    
    # Create a table to hold the characters
    table = [''] * num_cols
    for i in range(num_cols):
        table[i] = [''] * num_rows
    
    # Fill the table with characters from the encrypted message
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    index = 0
    for col in key_order:
        for row in range(num_rows):
            table[col][row] = encrypted_message[index]
            index += 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    
    # Read the rows to get the decrypted message
    decrypted_message = ''.join(
        table[col][row] for row in range(num_rows) for col in range(num_cols)
    )
    
    return decrypted_message

# Contoh penggunaan
if __name__ == "__main__":
    # Definisikan kunci substitusi
    key = '3142'  # Kunci yang menentukan urutan kolom

    # Pesan yang akan dienkripsi
    message = 'HELLO WORLD'

    # Enkripsi pesan
    encrypted = encrypt_transposition_cipher(message, key)

    # Dekripsi pesan
    decrypted = decrypt_transposition_cipher(encrypted, key)

    # Tampilkan hasil
    print(f'Original: {message}')
    print(f'Encrypted: {encrypted}')
    print(f'Decrypted: {decrypted}')
