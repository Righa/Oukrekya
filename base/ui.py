# Use common pyautogui stuff

import pyautogui, time

class MiGui():
	def __init__(self, app):
		self.app = app

	def pass_vars(self, mi_vars): #dict
		pass

	def wait_for_object(self, obj, patience=10, grayscale=True):
		time_out = patience
		print('I: waiting for button ...')
		while not (pyautogui.locateOnScreen(obj, grayscale=grayscale, confidence=0.8)):
			if time_out < 1:
				self.app.alerts.cry()
				time_out = patience
			time_out -= 1
			time.sleep(1)

	def wait_till_gone(self, obj, patience=10, grayscale=True):
		time_out = patience
		print('I: watching button ...')
		while (pyautogui.locateOnScreen(obj, grayscale=grayscale, confidence=0.8)):
			time_out -= 1
			if time_out < 1:
				self.app.alerts.cry()
				time_out = patience
			time.sleep(1)

	def click_till_gone(self):
		pass

	def click_x(self):
		time_out = 10
		print('I: closing paths')
		while pyautogui.locateOnScreen('rss/x_btn.png', confidence=0.8, grayscale=True):
			try:
				x, y = pyautogui.locateCenterOnScreen('rss/x_btn.png', confidence=0.8, grayscale=True)
				time.sleep(0.3)
				pyautogui.click(x=x, y=y)
				time_out -= 1
				if time_out < 1:
					self.app.alerts.cry()
					time_out = 10
			except TypeError:
				self.app.alerts.cry()
			time.sleep(1)

	def r3(self):
		pass

	def r5(self):
		pass

	def r6(self):
		pass

	def r7(self):
		pass

	def r8(self):
		pass