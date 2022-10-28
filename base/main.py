
import pyautogui, subprocess, time, screen_brightness_control

class MiApp():

	def run(self):

		subprocess.Popen('C:\\LDPlayer\\LDPlayer4.0\\dnplayer.exe')

		self.alerts.cry()

		lm_task = pyautogui.confirm(text='What you want to do?', title='Task' , buttons=['routine', 'shield'])

		self.start_with = pyautogui.confirm(text='What acc goes first?', title='Account' , buttons=self.accounts)

		if lm_task == 'shield':
			self.turf.shield_len = pyautogui.confirm(text='Choose bubble period', title='Shield duration' , buttons=['8h', '1d', '3d'])

		screen_brightness_control.set_brightness(1, display=0)

		print('I: opening game...')
		self.log.write('I: opening game... \n\n')

		self.guiman.wait_for_object('rss/app_icon.png', 100)

		print('S: emulator up and running...')
		self.log.write('S: emulator up and running... \n\n')

		time.sleep(3)
		x, y = pyautogui.locateCenterOnScreen('rss/app_icon.png', confidence=0.8, grayscale=True)
		time.sleep(0.3)
		pyautogui.click(x=x, y=y)

		self.login_wait()

		if lm_task == 'routine':
			self.turf.routine()
		elif lm_task == 'shield':
			self.turf.shield()
		elif lm_task == 'mkvk':
			kvk()
		elif lm_task == 'mdragon in':
			dragon_in()
		elif lm_task == 'mdragon out':
			dragon_out()
		else:
			print('S: More possibilities on the way ;)')
			self.log.write('S: More possibilities on the way ;) \n\n')

		self.alerts.cry()

		print('S: done')
		self.log.write('S: done! \n')

		self.log.close()

		screen_brightness_control.set_brightness(50, display=0)

	def login_wait(self):

		print('I: logging in ...')
		self.log.write('I: logging in ... \n\n')

		self.guiman.wait_for_object('rss/x_btn.png', 188)
		time.sleep(1)
		self.guiman.click_x()
		
