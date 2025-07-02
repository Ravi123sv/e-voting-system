import pyautogui
import time

# Wait 5 seconds to allow you to focus WhatsApp Web chat
print("You have 5 seconds to select the WhatsApp Web chat...")
time.sleep(5)

# Press Enter repeatedly every 0.3 seconds (about 3–4 times per second)
try:
    while True:
        pyautogui.press('enter')
        time.sleep(0.3)
except KeyboardInterrupt:
    print("Stopped.")

































