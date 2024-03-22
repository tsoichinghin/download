import random
import csv
import os
import shutil

def get_random_lowercase(length):
    lowercase_characters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numeric_characters = '1234567890'

    characters = lowercase_characters + uppercase_characters + numeric_characters
    result = ''
    for _ in range(length):
        random_index = random.randint(0, len(characters) - 1)
        result += characters[random_index]

    if any(c in result for c in lowercase_characters) and \
       any(c in result for c in uppercase_characters) and \
       any(c in result for c in numeric_characters):
        return result
    else:
        return get_random_lowercase(length)

min_length = 10
max_length = 15

while True:
    random_length = random.randint(min_length, max_length)
    random_string = get_random_lowercase(random_length)
    if isinstance(random_string, str) and random_string.strip() != '':
        break

csv_filename = os.path.join("pw.csv")
if os.path.exists(csv_filename):
    os.remove(csv_filename)
with open(csv_filename, "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([random_string])

destination_folder = "/home/tch/Desktop/uivision/datasources"
copy_file = os.path.join(destination_folder, "pw.csv")
if os.path.exists(copy_file):
    os.remove(copy_file)
shutil.copy(csv_filename, os.path.join(destination_folder, csv_filename))

