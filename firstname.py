import random
import csv
import os
import shutil

def get_random_lowercase(length):
    lowercase_characters = 'abcdefghijklmnopqrstuvwxyz'
    characters = lowercase_characters
    result = ''
    for _ in range(length):
        random_index = random.randint(0, len(characters) - 1)
        result += characters[random_index]
    return result

min_length = 4
max_length = 6

while True:
    random_length = random.randint(min_length, max_length)
    random_string = get_random_lowercase(random_length)
    if isinstance(random_string, str) and random_string.strip() != '':
        break

csv_filename = os.path.join("firstname.csv")
if os.path.exists(csv_filename):
    os.remove(csv_filename)
with open(csv_filename, "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([random_string])

destination_folder = "/home/tch/Desktop/uivision/datasources"
copy_file = os.path.join(destination_folder, "firstname.csv")
if os.path.exists(copy_file):
    os.remove(copy_file)
shutil.copy(csv_filename, os.path.join(destination_folder, csv_filename))

