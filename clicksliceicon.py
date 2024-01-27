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
def download_image(url, save_path):
    if not os.path.exists(save_path):
        response = requests.get(url)
        with open(save_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f"file {save_path} already exists. Skipping download.")
image_urls = [
    'https://i.imgur.com/Sh2o13F.png',
    'https://i.imgur.com/rAc6ef5.png',]
folder_path = "C:\\Users\\Administrator\\Downloads"
custom_names = ["slice1.png", "slice2.png"]
import cv2
import numpy as np
import pyautogui
slice1 = cv2.imread('slice1.png')
slice2 = cv2.imread('slice2.png')
screen_width, screen_height = pyautogui.size()
screenshot = pyautogui.screenshot()
screenshot_cv = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
result1 = cv2.matchTemplate(screenshot_cv, slice1, cv2.TM_CCOEFF_NORMED)
min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)
result2 = cv2.matchTemplate(screenshot_cv, slice2, cv2.TM_CCOEFF_NORMED)
min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)
threshold = 0.8
if max_val1 >= threshold or max_val2 >= threshold:
    if max_val1 >= threshold:
        match_loc = max_loc1
        matched_slice = slice1
    else:
        match_loc = max_loc2
        matched_slice = slice2
    match_x = match_loc[0] + matched_slice.shape[1] // 2
    match_y = match_loc[1] + matched_slice.shape[0] // 2
    pyautogui.click(match_x, match_y)
    print("Clicked at:", match_x, match_y)
else:
    print("No match found.")
