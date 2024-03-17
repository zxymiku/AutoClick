from pynput import keyboard, mouse
import pyautogui
import time

# 存储最后一次真实点击的位置和当前是否在模拟点击的状态
last_click_position = None
is_simulating_click = False


def on_click(x, y, button, pressed):
    global last_click_position, is_simulating_click

    if not is_simulating_click and button == mouse.Button.left and pressed:
        last_click_position = (x, y)
        simulate_double_click()


def simulate_double_click():
    global is_simulating_click

    if last_click_position is not None:
        is_simulating_click = True
        pyautogui.click(last_click_position[0], last_click_position[1], button='left', clicks=10)
        time.sleep(0.1)  # 确保模拟点击与下一次检测之间有足够的时间间隔
        is_simulating_click = False


def on_press(key):
    if key == keyboard.Key.f10:
        # 停止监听器并退出程序
        return False


# 启动鼠标监听器
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# 启动键盘监听器
with keyboard.Listener(on_press=on_press) as k_listener:
    k_listener.join()

# 在程序退出前，停止鼠标监听器（以防万一）
mouse_listener.stop()

