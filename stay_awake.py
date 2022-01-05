import pyautogui
import time

print(pyautogui.size())
pyautogui.FAILSAFE = False
pyautogui.moveTo(700, 500, duration = 1)
print("[+] Mouse moved at starting position")
while True:
	pyautogui.moveRel(0, 200, duration = 2)
	print("[+] Mouse moved at 200 rel")
	time.sleep(2)

	pyautogui.press("shift")
	print("[+] Shift key pressed")
	pyautogui.moveRel(0, -200, duration = 2)
	print("[+] Mouse moved at 200 rel")
	time.sleep(2)