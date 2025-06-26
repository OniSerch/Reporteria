# Flask_API/utils/brainfuck.py

def to_brainfuck(text):
    result = ''
    prev = 0
    for char in text:
        diff = ord(char) - prev
        if diff > 0:
            result += '+' * diff
        elif diff < 0:
            result += '-' * (-diff)
        result += '.'
        prev = ord(char)
    return result
