import subprocess
import os
try:
    subprocess.check_call(['pip', 'install', '--upgrade', 'Pillow'])
except subprocess.CalledProcessError as e:
    print(f"Error while installing/upgrading Pillow: {e}")
except FileNotFoundError:
    print("Cannot find pip command, please make sure Python is installed in the original system path")    
try:
    subprocess.check_call(['pip', 'install', 'requests'])
except subprocess.CalledProcessError as e:
    print(f"Error while installing requests: {e}")
except FileNotFoundError:
    print("Cannot find pip command, please make sure Python is installed in the original system path")
import requests
dependencies = ['pyautogui', 'opencv-python-headless', 'numpy']
for dependency in dependencies:
    try:
        subprocess.check_call(['pip', 'install', dependency])
    except subprocess.CalledProcessError as e:
         print(f"Error while installing {dependency}: {e}")
    except FileNotFoundError:
         print("Cannot find pip command, please make sure python is installed in the orignal system path")
animal_images_urls = [
    'https://i.imgur.com/Sh2o13F.png',
    'https://i.imgur.com/rAc6ef5.png',
    'https://i.imgur.com/yBK8V3N.png',
    'https://i.imgur.com/J1YVJ2s.png',
    'https://i.imgur.com/zICcqGP.png',
    'https://i.imgur.com/yXRcMe4.png',
    'https://i.imgur.com/ji17Kwi.png',
    'https://i.imgur.com/y6N8BPP.png',
    'https://i.imgur.com/ercdOHK.png']
slice_images_urls = [
    'https://i.imgur.com/tE04pZb.png',
    'https://i.imgur.com/sRT4Qis.png',]
animal_images_folder_path = "C:\\Users\\Administrator\\Downloads"
animal_images_custom_names = ["cat.png", "dog.png", "fox.png", "wolf.png", "monkey.png", "gorilla.png", "tiger.png", "lion.png", "civet.png"]
slice_images_folder_path = "C:\\Users\\Administrator\\Downloads"
slice_images_custom_names = ["slice1.png", "slice2.png"]
def download_animal_images(url, animal_images_save_path):
    if not os.path.exists(animal_images_save_path):
        response = requests.get(url)
        with open(animal_images_save_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"file {animal_images_save_path} already exists. Skipping download.")
for custom_name, url in zip(animal_images_custom_names, animal_images_urls):
    animal_images_save_path = os.path.join(animal_images_folder_path, custom_name)
    download_animal_images(url, animal_images_save_path)
def download_slice_images(url, slice_images_save_path):
    if not os.path.exists(slice_images_save_path):
        response = requests.get(url)
        with open(slice_images_save_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"file {slice_images_save_path} already exists. Skipping download.")
for custom_name, url in zip(slice_images_custom_names, slice_images_urls):
    slice_images_save_path = os.path.join(slice_images_folder_path, custom_name)
    download_slice_images(url, slice_images_save_path)