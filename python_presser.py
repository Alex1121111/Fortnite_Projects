import keyboard
import time
while(True):
	keyboard.press_and_release('e')
	time.sleep(0.01)
	if keyboard.is_pressed('q'):
		break