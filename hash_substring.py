# Anastasija Andrejeva, 18. grupa, 221RDC028

def read_input():
    input_type = input()

    if 'I' in input_type:
        pattern = input().strip()
        text = input().strip()
        return pattern, text
    
    elif 'F' in input_type:
        file = input()
        if not 'a' in file:
            file = "tests/" + file
            with open(file, 'r')as f:
                pattern = f.readline().strip()
                text = f.readline().strip()
                return pattern, text
    else:
        print("Ievadiet burtu 'I' vai 'F':")
        return


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    pattern_hash = 0
    for c in pattern:
        pattern_hash += ord(c)
    pattern_hash = pattern_hash % 101

    text_hash = 0
    for k in range(len(pattern)):
        text_hash += ord(text[k])
    text_hash = text_hash % 101

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

