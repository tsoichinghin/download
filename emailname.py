import random
import csv

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

csv_filename = "emailname.csv"
with open(csv_filename, "w", newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([random_string])

# 将CSV文件复制到指定位置
import shutil
import os

destination_folder = "/home/tch/Desktop/uivision/datasources"
shutil.copy(csv_filename, os.path.join(destination_folder, csv_filename))
