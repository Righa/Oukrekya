## imports

import pyautogui, subprocess, time, datetime

## vars

accounts = ['sneaky', 'lmara', 'imara', 'snaeky', 'gachiq', 'kibunja']

# kname oukrekya

# region(479, 269, 1441, 812), grayscale=True

# if time.strftime('%H:%M') < '21:00':

subprocess.Popen('C:\LDPlayer\LDPlayer4.0\dnplayer.exe')


## funcs

# waits for image to appear

def wait_for_icon_to_appear(img_btn, time_out=100, grayscale=True):
	print('I: waiting for button ...')
	while not (pyautogui.locateOnScreen(img_btn, region=(479, 269, 1441, 812), grayscale=grayscale, confidence=0.8) and time_out > 0):
		time_out -= 1
		time.sleep(1)

# waits for image to disappear

def wait_for_icon_to_disappear(img_btn, grayscale=True):
	print('I: watching button...')
	while (pyautogui.locateOnScreen(img_btn, region=(479, 269, 1441, 812), grayscale=grayscale, confidence=0.8)):
		time_out -= 1
		time.sleep(1)

# opens emulator and game

def open_game():
	print('opening game...')
	wait_for_icon_to_appear('rss/app_icon.png', 100)
	print('S: emulator up and running...')
	time.sleep(3)
	pyautogui.click('rss/app_icon.png')

# waits for game to open and dismisses spam popups

def login_wait():
	print('logging in ...')
	wait_for_icon_to_appear('rss/x_btn.png', 188)
	time.sleep(1)
	while pyautogui.locateOnScreen('rss/x_btn.png', confidence=0.8, region=(479, 269, 1441, 812), grayscale=True):
		x, y = pyautogui.locateCenterOnScreen('rss/x_btn.png', confidence=0.8, region=(479, 269, 1441, 812), grayscale=True)
		time.sleep(0.3)
		pyautogui.click(x=x, y=y)
		time.sleep(1)

# changes to given account

def switch_account(account):
	print('switching to '+account+' ...')
	pyautogui.click(x=1170, y=773)
	time.sleep(0.4)
	pyautogui.click(x=725, y=441)
	time.sleep(0.4)
	pyautogui.click(x=953, y=574)
	time.sleep(0.4)
	pyautogui.click(x=981, y=518)
	wait_for_icon_to_appear('rss/'+account+'.png', 100)
	time.sleep(0.1)
	pyautogui.click('rss/'+account+'.png')
	time.sleep(0.3)
	pyautogui.click('rss/ok_switch_account.png')
	time.sleep(1)
	wait_for_icon_to_appear('rss/confirm_switch.png', 100)
	time.sleep(0.1)
	pyautogui.click('rss/confirm_switch.png')
	print('logging in ...')
	time.sleep(8)
	login_wait()

# normal stuff

def routine():
	print('daily stuff...')
	login_wait()

	acc_num = 0

	for account in accounts:
		if acc_num > 0:
			switch_account(account)
		print('sweepin '+account+'...')

	print('do stuff here...')
	print('going back home...')
	switch_account('sneaky')

# shields all accounts

def shield():
	print('changing shields...')
	login_wait()

	acc_num = 0
	for account in accounts:
		if acc_num > 0:
			switch_account(account)

		print('bubblin '+account+' ...')
		pyautogui.click(x=1410, y=459)
		time.sleep(1)
		pyautogui.click(x=1282, y=561)
		time.sleep(1)

		if datetime.datetime.today().weekday() > 4:
			print('Weekend, shields already up!')
		elif time.strftime('%H:%M') < '21:00':
		    # 8h
			pyautogui.click(x=1216, y=544)
		elif datetime.datetime.today().weekday() == 4:
			# 3d
			pyautogui.click(x=1215, y=758)
		else:
		    # 1d
			pyautogui.click(x=1225, y=649)
		
		time.sleep(1)
		pyautogui.click(x=1033, y=531)
		time.sleep(1)
		pyautogui.click(x=1404, y=306)
		time.sleep(1)
		print('good, switching')
		acc_num += 1

	print('going back home...')
	switch_account('sneaky')

# prepares for kvk

def kvk_check():
	print('doing kvk...')
	login_wait()

	acc_num = 0

	for account in accounts:
		if acc_num > 0:
			switch_account(account)
		print('sweepin '+account+'...')

	print('going back home...')
	switch_account('sneaky')

# plays kvk

def kvk():
	print('doing kvk...')
	login_wait()

	# kvk_check()
	# lv4 region (x=861, y=445)(x=1056, y=636)

	runs = 0

	while runs < 5:
		acc_num = 0

		for account in accounts:
			if acc_num > 0:
				switch_account(account)
			print('sweepin '+account+'...')
			if runs == 0:
				pyautogui.click(x=744, y=359)

				while not pyautogui.locateOnScreen('rss/event_kvk.png', region=(479, 269, 1441, 812), grayscale=True, confidence=0.8):
					pyautogui.moveTo(x=846, y=490)
					pyautogui.drag(100, 0, duration=0.5)
					time.sleep(1)

				pyautogui.click('rss/event_kvk.png')
				pyautogui.click('rss/kvk_target.png')


		print('going back home...')
		switch_account('sneaky')
		runs +=1

# enters dragon

def dragon_in():
	print('entering dragon...')
	login_wait()

	acc_num = 0

	for account in accounts:
		if acc_num > 0:
			switch_account(account)
		print('sweepin '+account+'...')

	print('do stuff here...')
	print('going back home...')
	switch_account('sneaky')

# leaves dragon

def dragon_out():
	print('exiting dragon...')
	login_wait()

	acc_num = 0

	for account in accounts:
		if acc_num > 0:
			switch_account(account)
		print('sweepin '+account+'...')

	print('do stuff here...')
	print('going back home...')
	switch_account('sneaky')


## procedure

open_game()

lm_task = pyautogui.prompt(text='Choices: routine, shield, kvk, dragon in, dragon out', title='Task' , default='routine')

if lm_task == 'routine':
	routine()
elif lm_task == 'shield':
	shield()
elif lm_task == 'kvk':
	kvk()
elif lm_task == 'dragon in':
	dragon_in()
elif lm_task == 'dragon out':
	dragon_out()
else:
	print('More possibilities on the way ;)')

print('S: done')


