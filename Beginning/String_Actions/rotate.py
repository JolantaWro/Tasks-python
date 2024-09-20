def rotate(text, key):
    result = []
    
    lowercase_start = ord('a')
    lowercase_end = ord('z')
    uppercase_start = ord('A')
    uppercase_end = ord('Z')
    
    for char in text:
        if char.islower():
            shifted_char = chr((ord(char) - lowercase_start + key) % 26 + lowercase_start)
            result.append(shifted_char)
        elif char.isupper():
            shifted_char = chr((ord(char) - uppercase_start + key) % 26 + uppercase_start)
            result.append(shifted_char)
        else:
            result.append(char)
    
    return ''.join(result)
