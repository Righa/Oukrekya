import pyautogui, winsound, time

class Alerts():

	def cry(self):
		for i in range(3):
			winsound.Beep(999, 444)
			time.sleep(0.1)
		time.sleep(3)

	def opt(self, opt):
		if opt == 'task':
			return pyautogui.confirm(text='What you wanna do?', title='Task' , buttons=['routine', 'shield', 'kvk', 'dragon in', 'dragon out', 'cry'])
		elif opt == 'acc':
			return pyautogui.confirm(text='What you wanna do?', title='Task' , buttons=accounts)

	def acknowledge(self):
		alert(text='Press ok to continue', title='Still Here?', button='OK')
		

