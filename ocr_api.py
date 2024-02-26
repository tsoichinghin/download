import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/tch/Downloads/modern-webbing-403006-f1fb9897aa7d.json'
from google.cloud import vision
import pyautogui
import io

def detect_text(image):
    client = vision.ImageAnnotatorClient()

    # Convert the image to bytes
    with io.BytesIO() as output:
        image.save(output, format="PNG")
        content = output.getvalue()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")
   
    detected_text = ""  # 存储包含数字、符号和英文的文本
    for text in texts:
        description = text.description.strip()
        if any(c.isdigit() or c.isalpha() or c in "+-*/" for c in description):  # 检查文本是否包含数字、符号和英文
            detected_text += description + " "
            break
    if detected_text is None:
        print("No text detected.")
        return None

    print("Detected Text:", detected_text.strip())
    return detected_text.strip()

def capture_and_process():
    min_x, max_x = 440, 605
    min_y, max_y = 120, 190

# 读取屏幕截图
    screenshot = pyautogui.screenshot(region=(min_x, min_y, max_x - min_x, max_y - min_y))

    print(detect_text(screenshot))
    detected_text = detect_text(screenshot)
    if detected_text is not None:
        print("Detected Text:", detected_text)

# 将英文转换为数字
        text_to_number = {
            "zero": 0, "one": 1, "two": 2, "three": 3, "five": 5,
            "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13, "fifteen": 15,
            "twenty": 20
        }

        if "four" in detected_text and "teen" in detected_text:
            detected_text = detected_text.replace("fourteen", " 14 ")
        else:
            detected_text = detected_text.replace("four", " 4 ")

        if "six" in detected_text and "teen" in detected_text:
            detected_text = detected_text.replace("sixteen", " 16 ")
        else:
            detected_text = detected_text.replace("six", " 6 ")
        
        if "seven" in detected_text and "teen" in detected_text:
            detected_text = detected_text.replace("seventeen", " 17 ")
        else:
            detected_text = detected_text.replace("seven", " 7 ")
        
        if "eigh" in detected_text and "teen" in detected_text:
            detected_text = detected_text.replace("eighteen", " 18 ")
        else:
            detected_text = detected_text.replace("eigh", " 8 ")
        
        if "nine" in detected_text and "teen" in detected_text:
            detected_text = detected_text.replace("nineteen", " 19 ")
        else:
            detected_text = detected_text.replace("nine", " 9 ")

# 去除多余的空格
        detected_text = ' '.join(detected_text.split())

# 替换文本中的英文为数字
        for word, number in text_to_number.items():
            detected_text = detected_text.replace(word, str(number))
            print("Detected Text After Replacement:", detected_text)
        if any(c.isalpha() for c in detected_text):
            print("Alphabetic characters detected in replaced text. Removing them...")
            detected_text = ''.join(filter(lambda x: not x.isalpha(), detected_text))
        print("Final Detected Text After Replacement and Removal:", detected_text)

# 执行计算并输出结果
        result = eval(detected_text)
        print("Result:", result)

        return result
    
    else:
        print("No text detected.")
        return None

def compare_and_click_1(result):
    # 截取第二個範圍的屏幕截圖
    min_x, max_x = 615, 650
    min_y, max_y = 120, 190
    screenshot2 = pyautogui.screenshot(region=(min_x, min_y, max_x - min_x, max_y - min_y))

    # 檢測第二個範圍的數字
    detected_text_2 = detect_text(screenshot2)
    if detected_text_2:
        print("Detected Text 2:", detected_text_2)

        # 比對檢測到的數字與計算結果
        if str(result) in detected_text_2:
            print("Result found in Detected Text 2. Clicking...")
            pyautogui.doubleClick(632, 157)
            return True
        else:
            print("Result not found in Detected Text 2.")
            return False
    else:
        print("No text detected in screenshot 2.")
        return False

def compare_and_click_2(result):
    # 截取第二個範圍的屏幕截圖
    min_x, max_x = 650, 680
    min_y, max_y = 120, 190
    screenshot3 = pyautogui.screenshot(region=(min_x, min_y, max_x - min_x, max_y - min_y))

    # 檢測第二個範圍的數字
    detected_text_3 = detect_text(screenshot3)
    if detected_text_3:
        print("Detected Text 3:", detected_text_3)

        # 比對檢測到的數字與計算結果
        if str(result) in detected_text_3:
            print("Result found in Detected Text 3. Clicking...")
            pyautogui.doubleClick(665, 157)
            return True
        else:
            print("Result not found in Detected Text 3.")
            return False
    else:
        print("No text detected in screenshot 3.")
        return False

def compare_and_click_3(result):
    # 截取第二個範圍的屏幕截圖
    min_x, max_x = 680, 720
    min_y, max_y = 120, 190
    screenshot4 = pyautogui.screenshot(region=(min_x, min_y, max_x - min_x, max_y - min_y))

    # 檢測第二個範圍的數字
    detected_text_4 = detect_text(screenshot4)
    if detected_text_4:
        print("Detected Text 4:", detected_text_4)

        # 比對檢測到的數字與計算結果
        if str(result) in detected_text_4:
            print("Result found in Detected Text 4. Clicking...")
            pyautogui.doubleClick(700, 155)
            return True
        else:
            print("Result not found in Detected Text 4.")
            return False
    else:
        print("No text detected in screenshot 4.")
        return False

result = capture_and_process()
if result is not None:
    if compare_and_click_1(result):
        pass
    elif compare_and_click_2(result):
        pass
    elif compare_and_click_3(result):
        pass
    else:
        print("Result not found in any Detected Text.")