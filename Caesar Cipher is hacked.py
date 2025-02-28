def decrypt_message(encrypted_message, n, real_char):
    no_space_message = ''.join([char for char in encrypted_message if char != ' '])
    space_indices = [i for i, char in enumerate(encrypted_message) if char == ' ']

    index = n - 1

    shift = (ord(no_space_message[index]) - ord(real_char)) % 26

    decrypted_message = list(no_space_message)

    for i in range(len(no_space_message)):
        current_shift = (shift + (i - index)) % 26
        if i < index:
            current_shift = (shift - (index - i)) % 26
        decrypted_message[i] = chr((ord(no_space_message[i]) - ord('a') - current_shift) % 26 + ord('a'))

    result = ''.join(decrypted_message)

    for i in space_indices:
        result = result[:i] + ' ' + result[i:]

    return result

encrypted_message = input()
n = int(input())
real_char = input()

result = decrypt_message(encrypted_message, n, real_char)
print(result)
