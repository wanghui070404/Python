def generate_playfair_matrix(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # J is omitted
    matrix = []

    # Remove duplicates from keyword
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    for char in keyword.upper():
        if char in alphabet:
            alphabet = alphabet.replace(char, '')
            matrix.append(char)

    matrix += alphabet

    return [matrix[i:i+5] for i in range(0, 25, 5)]  # range(start, stop, step)
# Divide the input to two letter set


def playfair_digraphs(text):
    digraphs = []
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            digraphs.append((text[i], 'X'))
            break
        if text[i] == text[i+1]:
            digraphs.append((text[i], 'X'))
            i += 1
        else:
            digraphs.append((text[i], text[i+1]))
            i += 2
    return digraphs
# Encryp plaintext


def playfair_encrypt(text, keyword):
    matrix = generate_playfair_matrix(keyword)
    digraphs = playfair_digraphs(text.replace('J', 'I').upper())
    encrypted = ""

    for digraph in digraphs:
        row1, col1, row2, col2 = -1, -1, -1, -1
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == digraph[0]:
                    row1, col1 = i, j
                if matrix[i][j] == digraph[1]:
                    row2, col2 = i, j

        if row1 == row2:
            # circle shift row
            encrypted += matrix[row1][(col1+1) %
                                      5] + matrix[row2][(col2+1) % 5]
        elif col1 == col2:
            encrypted += matrix[(row1+1) % 5][col1] + \
                matrix[(row2+1) % 5][col2]  # circle shift collumn
        else:
            encrypted += matrix[row1][col2] + \
                matrix[row2][col1]  # Diagonal line

    return encrypted


def playfair_decrypt(text, keyword):
    matrix = generate_playfair_matrix(keyword)
    digraphs = playfair_digraphs(text.replace('J', 'I').upper())
    decrypted = ""

    for digraph in digraphs:
        row1, col1, row2, col2 = -1, -1, -1, -1
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == digraph[0]:
                    row1, col1 = i, j
                if matrix[i][j] == digraph[1]:
                    row2, col2 = i, j

        if row1 == row2:
            decrypted += matrix[row1][mod5(col1-1)] + \
                matrix[row2][mod5(col2-1)]
        elif col1 == col2:
            decrypted += matrix[mod5(row1-1)][col1] + \
                matrix[mod5(row2-1)][col2]
        else:
            decrypted += matrix[row1][col2] + matrix[row2][col1]

    return decrypted


def mod5(n):
    return (n + 5) % 5


if __name__ == "__main__":
    # Example usage:
    plaintext = "Buoihocthubavematmahoc"
    keyword = "UITTHEBESTFORJOBS"
    matrix = generate_playfair_matrix(keyword)
    for row in matrix:
        print(' '.join(row))
    digraphs = playfair_digraphs(plaintext.replace('J', 'I').upper())
    for pair in digraphs:
        print(pair)
    encrypted = playfair_encrypt(plaintext, keyword)
    decrypted = playfair_decrypt(encrypted, keyword)
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
