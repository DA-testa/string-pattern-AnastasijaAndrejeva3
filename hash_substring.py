# python3

def read_input():
    input_type = input()

    if input_type == 'I':
        pattern = input().strip()
        text = input().strip()
    if input_type = 'F':
        with open('tests.txt', 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        pass

    return pattern, text


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    pattern_hash = sum(ord(c) for c in pattern) % 101
    text_hash = sum(ord(text[i]) for i in range(len(pattern))) % 101

    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+len(pattern)]:
                occurrences.append(i)
        if i < len(text) - len(pattern):
            text_hash = text_hash - ord(text[i]) + ord(text[i+len(pattern)])
            text_hash %= 101
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

