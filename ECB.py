def encrypt_ecb(plaintext_hex, key_binary):
    # Konversi plaintext hex ke binary
    binary_plaintext = bin(int(plaintext_hex, 16))[2:]

    # Bagi plainteks menjadi blok-blok 4 bit
    bit_blocks = [binary_plaintext[i:i + 4] for i in range(0, len(binary_plaintext), 4)]

    # Enkripsi ECB
    encrypted_blocks = []
    for bit_block in bit_blocks:
        # Operasi XOR Dengan Kuncinya
        xor_result = ''.join(str((int(bit) + int(key_bit)) % 2) for bit, key_bit in zip(bit_block, key_binary))

        # Geser 1 bit ke kiri
        shifted_result = xor_result[1:] + xor_result[0]

        # Konversi hasil XOR yang digeser ke desimal dan tambahkan ke hasil enkripsi
        encrypted_blocks.append(str(int(shifted_result, 2)))

    return encrypted_blocks

# Input dari pengguna
plaintext_hex = input("Masukkan plaintext (Hex): ")
key_binary = input("Masukkan kunci (Biner): ")

# Enkripsi ECB
encrypted_blocks = encrypt_ecb(plaintext_hex, key_binary)

# Mencetak hasilnya
print("\n-------- Hasil Enkripsi ECB --------")
print("| Plaintext (Hex):", plaintext_hex)
print("| Key (Biner):", key_binary)
print("| Encrypted Blocks:", encrypted_blocks)
print("------------------------------------")
