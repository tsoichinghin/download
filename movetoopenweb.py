import pyautogui
import random
from pyHM import mouse

# 获取屏幕分辨率
screen_width, screen_height = pyautogui.size()

# 定义指定座标范围
min_x, max_x = 160, 230
min_y, max_y = 62, 66

# 获取当前鼠标位置
current_x, current_y = pyautogui.position()

# 移动鼠标到指定范围内的随机位置
final_x = random.randint(min_x, max_x)
final_y = random.randint(min_y, max_y)

speed = random.uniform(2.5, 4.5) 

mouse.move(final_x, final_y, multiplier=speed)

mouse.click(final_x, final_y)