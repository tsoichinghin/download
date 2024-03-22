import random

def get_random_lowercase(length):
    lowercase_characters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    characters = lowercase_characters + uppercase_characters
    result = ''
    for _ in range(length):
        random_index = random.randint(0, len(characters) - 1)
        result += characters[random_index]
    return result

min_length = 10
max_length = 15

while True:
    random_length = random.randint(min_length, max_length)
    random_string = get_random_lowercase(random_length)
    if isinstance(random_string, str) and random_string.strip() != '':
        break

print(random_string)
