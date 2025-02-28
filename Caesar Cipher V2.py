def encrypt_sentence(initial_shift, sentence):
    encrypted_sentence = ""
    current_shift = initial_shift
    for char in sentence:
        if char == " ":
            encrypted_sentence += " "
        else:
            new_char = chr((ord(char) - ord('a') + current_shift) % 26 + ord('a'))
            encrypted_sentence += new_char
            current_shift += 1
    return encrypted_sentence

initial_shift = int(input())
sentence = input()
result = encrypt_sentence(initial_shift, sentence)
print( result)
