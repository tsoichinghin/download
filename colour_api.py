import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/tch/Downloads/modern-webbing-403006-f1fb9897aa7d.json'
import math
from google.cloud import vision
import pyautogui

def save_screenshot(image, filepath):
    image.save(filepath)

def euclidean_distance(color1, color2):
    r1, g1, b1 = color1.red, color1.green, color1.blue
    r2, g2, b2 = color2.red, color2.green, color2.blue
    return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

def detect_properties(image_path):
    client = vision.ImageAnnotatorClient()
    with open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    print("Properties:")
    colors = []
    for color in props.dominant_colors.colors:
        print(f"R: {color.color.red}, G: {color.color.green}, B: {color.color.blue}")
        colors.append(color.color)
    return colors

def compare_colors_1and2(colors1, colors2):
    similar_count = 0
    total_count = min(len(colors1), len(colors2))
    if total_count != 0:
        similarity_percentage = similar_count / total_count
    else:
        similarity_percentage = 0  # 或者采取其他适当的处理方式

    for color1, color2 in zip(colors1, colors2):
        distance = euclidean_distance(color1, color2)
        similarity = 1 - (distance / 255)  # Convert distance to similarity percentage
        if similarity > 0.85:  # Adjust this threshold as needed
            similar_count += 1
    
    similarity_percentage = "{:.2f}".format(similarity_percentage)
    similarity_percentage = similar_count / total_count  # Check if similarity percentage is greater than 80%
    print('compare_colors_1and2:', similarity_percentage)
    if similarity_percentage > 0.3:
        print('compare_colors_1and2 = Click, similarity_percentage > 0.3')
        pyautogui.doubleClick(502,151)
        return True
    else:
        print('compare_colors_1and2 = Dont click, similarity_percentage < 0.3')
        return False
    
def compare_colors_1and3(colors1, colors3):
    similar_count = 0
    total_count = min(len(colors1), len(colors3))
    if total_count != 0:
        similarity_percentage = similar_count / total_count
    else:
        similarity_percentage = 0  # 或者采取其他适当的处理方式

    for color1, color3 in zip(colors1, colors3):
        distance = euclidean_distance(color1, color3)
        similarity = 1 - (distance / 255)  # Convert distance to similarity percentage
        if similarity > 0.85:  # Adjust this threshold as needed
            similar_count += 1
    
    similarity_percentage = "{:.2f}".format(similarity_percentage)
    similarity_percentage = similar_count / total_count  # Check if similarity percentage is greater than 80%
    print('compare_colors_1and3:', similarity_percentage)
    if similarity_percentage > 0.3:
        print('compare_colors_1and3 = Click, similarity_percentage > 0.3')
        pyautogui.doubleClick(502,151)
        return True
    else:
        print('compare_colors_1and3 = Dont click, similarity_percentage < 0.3')
        return False

def compare_colors_1and4(colors1, colors4):
    similar_count = 0
    total_count = min(len(colors1), len(colors4))
    if total_count != 0:
        similarity_percentage = similar_count / total_count
    else:
        similarity_percentage = 0  # 或者采取其他适当的处理方式

    for color1, color4 in zip(colors1, colors4):
        distance = euclidean_distance(color1, color4)
        similarity = 1 - (distance / 255)  # Convert distance to similarity percentage
        if similarity > 0.85:  # Adjust this threshold as needed
            similar_count += 1

    similarity_percentage = "{:.2f}".format(similarity_percentage)
    similarity_percentage = similar_count / total_count  # Check if similarity percentage is greater than 80%
    print('compare_colors_1and4:', similarity_percentage)
    if similarity_percentage > 0.3:
        print('compare_colors_1and4 = Click, similarity_percentage > 0.3')
        pyautogui.doubleClick(502,151)
        return True
    else:
        print('compare_colors_1and4 = Dont click, similarity_percentage < 0.3')
        return False

def compare_colors_1and5(colors1, colors5):
    similar_count = 0
    total_count = min(len(colors1), len(colors5))
    if total_count != 0:
        similarity_percentage = similar_count / total_count
    else:
        similarity_percentage = 0  # 或者采取其他适当的处理方式

    for color1, color5 in zip(colors1, colors5):
        distance = euclidean_distance(color1, color5)
        similarity = 1 - (distance / 255)  # Convert distance to similarity percentage
        if similarity > 0.85:  # Adjust this threshold as needed
            similar_count += 1

    similarity_percentage = "{:.2f}".format(similarity_percentage)
    similarity_percentage = similar_count / total_count  # Check if similarity percentage is greater than 80%
    print('compare_colors_1and5:',similarity_percentage)
    if similarity_percentage > 0.3:
        print('compare_colors_1and5 = Click, similarity_percentage > 0.3')
        pyautogui.doubleClick(502,151)
        return True
    else:
        print('compare_colors_1and5 = Dont click, similarity_percentage < 0.3')
        return False
    
def compare_colors_2and3(colors2, colors3):
    similar_count = 0
    total_count = min(len(colors2), len(colors3))
    if total_count != 0:
        similarity_percentage = similar_count / total_count
    else:
        similarity_percentage = 0  # 或者采取其他适当的处理方式

    for color2, color3 in zip(colors2, colors3):
        distance = euclidean_distance(color2, color3)
        similarity = 1 - (distance / 255)  # Convert distance to similarity percentage
        if similarity > 0.85:  # Adjust this threshold as needed
            similar_count += 1

    similarity_percentage = "{:.2f}".format(similarity_percentage)
    similarity_percentage = similar_count / total_count  # Check if similarity percentage is greater than 80%
    print('compare_colors_2and3:', similarity_percentage)
    if similarity_percentage > 0.3:
        print('compare_colors_2and3 = Click, similarity_percentage > 0.3')
        pyautogui.doubleClick(557,151)
        return True
    else:
        print('compare_colors_2and3 = Dont click, similarity_percentage < 0.3')
        return False
    
def compare_colors_2and4(colors2, colors4):
    similar_count = 0
    total_count = min(len(colors2), len(colors4))
    if total_count != 0:
        similarity_percentage = similar_count / total_count
    else:
        similarity_percentage = 0  # 或者采取其他适当的处理方式

    for color2, color4 in zip(colors2, colors4):
        distance = euclidean_distance(color2, color4)
        similarity = 1 - (distance / 255)  # Convert distance to similarity percentage
        if similarity > 0.85:  # Adjust this threshold as needed
            similar_count += 1

    similarity_percentage = "{:.2f}".format(similarity_percentage)
    similarity_percentage = similar_count / total_count  # Check if similarity percentage is greater than 80%
    print('compare_colors_2and4:', similarity_percentage)
    if similarity_percentage > 0.3:
        print('compare_colors_2and4 = Click, similarity_percentage > 0.3')
        pyautogui.doubleClick(557,151)
        return True
    else:
        print('compare_colors_2and4 = Dont click, similarity_percentage < 0.3')
        return False

def compare_colors_2and5(colors2, colors5):
    similar_count = 0
    total_count = min(len(colors2), len(colors5))
    if total_count != 0:
        similarity_percentage = similar_count / total_count
    else:
        similarity_percentage = 0  # 或者采取其他适当的处理方式

    for color2, color5 in zip(colors2, colors5):
        distance = euclidean_distance(color2, color5)
        similarity = 1 - (distance / 255)  # Convert distance to similarity percentage
        if similarity > 0.85:  # Adjust this threshold as needed
            similar_count += 1

    similarity_percentage = "{:.2f}".format(similarity_percentage)
    similarity_percentage = similar_count / total_count  # Check if similarity percentage is greater than 80%
    print('compare_colors_2and5:', similarity_percentage)
    if similarity_percentage > 0.3:
        print('compare_colors_2and5 = Click, similarity_percentage > 0.3')
        pyautogui.doubleClick(557,151)
        return True
    else:
        print('compare_colors_2and5 = Dont click, similarity_percentage < 0.3')
        return False

def compare_colors_3and4(colors3, colors4):
    similar_count = 0
    total_count = min(len(colors3), len(colors4))
    if total_count != 0:
        similarity_percentage = similar_count / total_count
    else:
        similarity_percentage = 0  # 或者采取其他适当的处理方式

    for color3, color4 in zip(colors3, colors4):
        distance = euclidean_distance(color3, color4)
        similarity = 1 - (distance / 255)  # Convert distance to similarity percentage
        if similarity > 0.85:  # Adjust this threshold as needed
            similar_count += 1

    similarity_percentage = "{:.2f}".format(similarity_percentage)
    similarity_percentage = similar_count / total_count  # Check if similarity percentage is greater than 80%
    print('compare_colors_3and4:', similarity_percentage)
    if similarity_percentage > 0.3:
        print('compare_colors_3and4 = Click, similarity_percentage > 0.3')
        pyautogui.doubleClick(612,151)
        return True
    else:
        print('compare_colors_3and4 = Dont click, similarity_percentage < 0.3')
        return False

def compare_colors_3and5(colors3, colors5):
    similar_count = 0
    total_count = min(len(colors3), len(colors5))
    if total_count != 0:
        similarity_percentage = similar_count / total_count
    else:
        similarity_percentage = 0  # 或者采取其他适当的处理方式

    for color3, color5 in zip(colors3, colors5):
        distance = euclidean_distance(color3, color5)
        similarity = 1 - (distance / 255)  # Convert distance to similarity percentage
        if similarity > 0.85:  # Adjust this threshold as needed
            similar_count += 1

    similarity_percentage = "{:.2f}".format(similarity_percentage)
    similarity_percentage = similar_count / total_count  # Check if similarity percentage is greater than 80%
    print('compare_colors_3and5:', similarity_percentage)
    if similarity_percentage > 0.3:
        print('compare_colors_3and5 = Click, similarity_percentage > 0.3')
        pyautogui.doubleClick(612,151)
        return True
    else:
        print('compare_colors_3and5 = Dont click, similarity_percentage < 0.3')
        return False

def compare_colors_4and5(colors4, colors5):
    similar_count = 0
    total_count = min(len(colors4), len(colors5))
    if total_count != 0:
        similarity_percentage = similar_count / total_count
    else:
        similarity_percentage = 0  # 或者采取其他适当的处理方式

    for color4, color5 in zip(colors4, colors5):
        distance = euclidean_distance(color4, color5)
        similarity = 1 - (distance / 255)  # Convert distance to similarity percentage
        if similarity > 0.85:  # Adjust this threshold as needed
            similar_count += 1

    similarity_percentage = "{:.2f}".format(similarity_percentage)
    similarity_percentage = similar_count / total_count  # Check if similarity percentage is greater than 80%
    print('compare_colors_4and5:', similarity_percentage)
    if similarity_percentage > 0.3:
        print('compare_colors_4and5 = Click, similarity_percentage > 0.3')
        pyautogui.doubleClick(667,151)
        return True
    else:
        print('compare_colors_4and5 = Dont click, similarity_percentage < 0.3')
        return False

screenshot1_min_x, screenshot1_max_x = 475, 530
screenshot1_min_y, screenshot1_max_y = 124, 179
screenshot1 = pyautogui.screenshot(region=(screenshot1_min_x, screenshot1_min_y, screenshot1_max_x - screenshot1_min_x, screenshot1_max_y - screenshot1_min_y))
screenshot1_filepath = '/home/tch/Downloads/screenshot1.png'
save_screenshot(screenshot1, screenshot1_filepath)

screenshot2_min_x, screenshot2_max_x = 530, 585
screenshot2_min_y, screenshot2_max_y = 124, 179
screenshot2 = pyautogui.screenshot(region=(screenshot2_min_x, screenshot2_min_y, screenshot2_max_x - screenshot2_min_x, screenshot2_max_y - screenshot2_min_y))
screenshot2_filepath = '/home/tch/Downloads/screenshot2.png'
save_screenshot(screenshot2, screenshot2_filepath)

screenshot3_min_x, screenshot3_max_x = 585, 640
screenshot3_min_y, screenshot3_max_y = 124, 179
screenshot3 = pyautogui.screenshot(region=(screenshot3_min_x, screenshot3_min_y, screenshot3_max_x - screenshot3_min_x, screenshot3_max_y - screenshot3_min_y))
screenshot3_filepath = '/home/tch/Downloads/screenshot3.png'
save_screenshot(screenshot3, screenshot3_filepath)

screenshot4_min_x, screenshot4_max_x = 640, 695
screenshot4_min_y, screenshot4_max_y = 124, 179
screenshot4 = pyautogui.screenshot(region=(screenshot4_min_x, screenshot4_min_y, screenshot4_max_x - screenshot4_min_x, screenshot4_max_y - screenshot4_min_y))
screenshot4_filepath = '/home/tch/Downloads/screenshot4.png'
save_screenshot(screenshot4, screenshot4_filepath)

screenshot5_min_x, screenshot5_max_x = 695, 750
screenshot5_min_y, screenshot5_max_y = 124, 179
screenshot5 = pyautogui.screenshot(region=(screenshot5_min_x, screenshot5_min_y, screenshot5_max_x - screenshot5_min_x, screenshot5_max_y - screenshot5_min_y))
screenshot5_filepath = '/home/tch/Downloads/screenshot5.png'
save_screenshot(screenshot5, screenshot5_filepath)

colors1 = detect_properties('/home/tch/Downloads/screenshot1.png')
colors2 = detect_properties('/home/tch/Downloads/screenshot2.png')
colors3 = detect_properties('/home/tch/Downloads/screenshot3.png')
colors4 = detect_properties('/home/tch/Downloads/screenshot4.png')
colors5 = detect_properties('/home/tch/Downloads/screenshot5.png')

if compare_colors_1and2(colors1, colors2):
    pass
elif compare_colors_1and3(colors1, colors3):
    pass
elif compare_colors_1and4(colors1, colors4):
    pass
elif compare_colors_1and5(colors1, colors5):
    pass
elif compare_colors_2and3(colors2, colors3):
    pass
elif compare_colors_2and4(colors2, colors4):
    pass
elif compare_colors_2and5(colors2, colors5):
    pass
elif compare_colors_3and4(colors3, colors4):
    pass
elif compare_colors_3and5(colors3, colors5):
    pass
elif compare_colors_4and5(colors4, colors5):
    pass
else:
    print("None of images are matched.")
    