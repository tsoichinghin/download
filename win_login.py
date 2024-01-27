import cv2
import pyautogui
import time
import numpy as np
check_images = [
    cv2.imread("C:\\Users\\Administrator\\Downloads\\dog.png"),
    cv2.imread("C:\\Users\\Administrator\\Downloads\\wolf.png"),
    cv2.imread("C:\\Users\\Administrator\\Downloads\\civet.png"),
    cv2.imread("C:\\Users\\Administrator\\Downloads\\cat.png"),
    cv2.imread("C:\\Users\\Administrator\\Downloads\\monkey.png"),
    cv2.imread("C:\\Users\\Administrator\\Downloads\\tiger.png"),
    cv2.imread("C:\\Users\\Administrator\\Downloads\\lion.png"),
    cv2.imread("C:\\Users\\Administrator\\Downloads\\fox.png"),
    cv2.imread("C:\\Users\\Administrator\\Downloads\\gorilla.png")]
scroll_image_path = (840, 698)
scroll_position = scroll_image_path
width_in_cm = 12
height_in_cm = 10
width_in_pixels = int(width_in_cm * 25.4 / 2.54)
height_in_pixels = int(height_in_cm * 25.4 / 2.54)
fixed_head_position = (960, 570)
repetitions = 230
def find_animal_head(fixed_head_position):
    target_position = fixed_head_position
    print("Animal Head Position:", target_position)
def calculate_similarity(screen_image, correct_direction_image):
    result = cv2.matchTemplate(screen_image, correct_direction_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return max_val
def is_animal_head_direction_correct(check_images):
    print("Entering is_animal_head_direction_correct")
    print("Check images paths:", check_images)
    for image_path in check_images:
        try:
            check_image = cv2.imread(image_path)
            if check_image is None:
                print(f"Failed to load image from path: {image_path}")
                continue
        except Exception as e:
            print(f"Error loading image from path {image_path}: {e}")
            continue
        if check_image is not None:
            print(f"Image loaded successfully from path: {image_path}")
            print("Check image shape:", check_image.shape)
    screenshot = pyautogui.screenshot(region=(
        fixed_head_position[0] - width_in_pixels // 2,
        fixed_head_position[1] - height_in_pixels // 2,
        width_in_pixels,
        height_in_pixels
    )).convert('RGB')
    screen_image = np.array(screenshot, dtype=np.uint8)
    print("Screen image width:", width_in_pixels, "height:", height_in_pixels)
    for check_image in check_images:
        print("Screen image shape:", screen_image.shape)
        print("check image shape:", check_image.shape)
        print("check image width:", check_image.shape[1], "height:", check_image.shape[0])
        similarity = calculate_similarity(screen_image, check_image)
        print("Similarity:", similarity)
        if similarity > 0.8:
            print("Correct Direction Detected")
            return True
    print("Incorrect Direction Detected")
    print("Exiting is_animal_head_direction_correct")
    return False
def simulate_scroll_and_rotate(repetitions, fixed_head_position, scroll_position):
    scroll_increment = 1
    current_repetition = 0
    while current_repetition < repetitions:        
        print("Entering simulate_scroll_and_rotate")
        start_position = scroll_position
        print("Start Position:", start_position)
        pyautogui.mouseDown(start_position[0], start_position[1])
        pyautogui.moveTo(start_position[0] + scroll_increment, start_position[1], duration=0.1)
        time.sleep(1)
        find_animal_head(fixed_head_position)
        if is_animal_head_direction_correct(check_images):
            pyautogui.mouseUp()
            print("Correct Direction Detected. Exiting simulate_scroll_and_rotate")
            return
        scroll_increment += 1
        current_repetition += 1
simulate_scroll_and_rotate(repetitions, fixed_head_position, scroll_position)