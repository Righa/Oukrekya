class KVK():
	def __init__(self, app):
		self.app = app

	def enter_kvk(self):
		print('I: doing kvk...')
		login_wait()

		# kvk_check()
		# lv4 region (x=861, y=445)(x=1056, y=636)

		runs = 0

		while runs < 5:
			acc_num = accounts.index(start_with)

			for account in accounts:
				if acc_num > 0:
					self.app.turf.switch_account(account)
				print('I: sweepin '+account+'...')
				if runs == 0:
					pyautogui.click(x=744, y=359)

					while not pyautogui.locateOnScreen('rss/event_kvk.png', grayscale=True, confidence=0.8):
						pyautogui.moveTo(x=846, y=490)
						pyautogui.drag(100, 0, duration=0.5)
						time.sleep(1)

					pyautogui.click('rss/event_kvk.png')
					pyautogui.click('rss/kvk_target.png')


			print('I: going back home...')
			self.app.turf.switch_account('sneaky')
			runs +=1

	def leave_kvk(self):
		print('I: leaving kvk...')


class Dragon():
	def __init__(self, app):
		self.app = app

	def enter_arena(self):
		print('I: Entering arena...')

	def leave_arena(self):
		print('I: Leaving arena...')
		