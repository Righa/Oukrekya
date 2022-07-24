## imports

import pyautogui, subprocess, time, datetime, winsound, json

## import guide

guide_json = open('guide.json')
guide = json.load(guide_json)

## vars

accounts = [*guide['accounts'].keys()]

# recovery vars

start_with = ''

subprocess.Popen('C:\LDPlayer\LDPlayer4.0\dnplayer.exe')


## funcs

# gives alert beep

def cry():
	for i in range(3):
		winsound.Beep(999, 444)
		time.sleep(0.1)

# waits for image to appear

def wait_for_icon_to_appear(img_btn, time_out=100, grayscale=True):
	print('I: waiting for button ...')
	while not (pyautogui.locateOnScreen(img_btn, grayscale=grayscale, confidence=0.8) and time_out > 0):
		time_out -= 1
		time.sleep(1)

# waits for image to disappear

def wait_for_icon_to_disappear(img_btn, time_out=100, grayscale=True):
	print('I: watching button...')
	while (pyautogui.locateOnScreen(img_btn, grayscale=grayscale, confidence=0.8) and time_out > 0):
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
	while pyautogui.locateOnScreen('rss/x_btn.png', confidence=0.8, grayscale=True):
		x, y = pyautogui.locateCenterOnScreen('rss/x_btn.png', confidence=0.8, grayscale=True)
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
	wait_for_icon_to_appear('accounts/'+account+'.png', 100)
	time.sleep(0.1)
	pyautogui.click('accounts/'+account+'.png')
	time.sleep(0.3)
	pyautogui.click('accounts/ok_switch_account.png')
	time.sleep(1)
	wait_for_icon_to_appear('accounts/confirm_switch.png', 100)
	time.sleep(0.1)
	pyautogui.click('accounts/confirm_switch.png')
	print('logging in ...')
	time.sleep(8)
	login_wait()

# collect gifts

def collect_gifts(account):
	print('collecting gifts')
	time.sleep(0.3)
	pyautogui.click(x=927, y=775)
	time.sleep(3)
	pyautogui.click(x=1370, y=412)
	time.sleep(1)
	pyautogui.click(x=1206, y=481)
	time.sleep(1.9)
	pyautogui.click(x=1235, y=454)
	time.sleep(1)

	if guide['accounts'][account]['vip']:
		wait_for_icon_to_appear('guild/open_all_gifts.png')
		x, y = pyautogui.locateCenterOnScreen('guild/open_all_gifts.png', confidence=0.8, grayscale=True)
		pyautogui.click(x=x, y=y)
		time.sleep(3)
		x, y = pyautogui.locateCenterOnScreen('guild/delete_all.png', confidence=0.8, grayscale=True)
		pyautogui.click(x=x, y=y)
		wait_for_icon_to_appear('guild/no_bonus_chests.png')
		time.sleep(1)
		pyautogui.click(x=979, y=449)
		wait_for_icon_to_disappear('guild/no_bonus_chests.png')
		time.sleep(3)
		wait_for_icon_to_appear('guild/open_all_gifts.png')
		x, y = pyautogui.locateCenterOnScreen('guild/open_all_gifts.png', confidence=0.8, grayscale=True)
		pyautogui.click(x=x, y=y)
		time.sleep(3)
		x, y = pyautogui.locateCenterOnScreen('guild/delete_all.png', confidence=0.8, grayscale=True)
		pyautogui.click(x=x, y=y)
		wait_for_icon_to_appear('guild/no_guild_gifts.png')

	else:
		pyautogui.click(x=1463, y=467)
		time.sleep(1)
		pyautogui.click(x=1137, y=457)
		time.sleep(1)
		pyautogui.click(x=1221, y=332)
		wait_for_icon_to_appear('guild/no_bonus_chests.png')
		time.sleep(3)
		pyautogui.click(x=1207, y=254)
		time.sleep(3)
		
		pyautogui.click(x=979, y=449)
		time.sleep(1)
		pyautogui.click(x=1463, y=467)
		time.sleep(0.3)
		pyautogui.click(x=1137, y=457)
		time.sleep(0.3)
		pyautogui.click(x=1221, y=332)
		wait_for_icon_to_appear('guild/no_guild_gifts.png')
		pyautogui.click(x=1207, y=254)

	time.sleep(1)
	pyautogui.click(x=1404, y=306)
	time.sleep(1)
	pyautogui.click(x=1404, y=306)
	time.sleep(3)
	evd = pyautogui.screenshot(region=(479, 269, 963, 543))
	evd.save(r'C:\Users\lawrencie\Desktop\reports\guild\\'+account+'.png')

# send help

def send_help():
	print('helping')
	if pyautogui.locateOnScreen('turf/help.png', confidence=0.7):
		time.sleep(1)
		x,y = pyautogui.locateCenterOnScreen('turf/help.png', confidence=0.7)
		pyautogui.click(x=x, y=y)
		time.sleep(1)
		pyautogui.click(x=955, y=766)
		time.sleep(1)
		pyautogui.click(x=1404, y=306)

# quests

def quests():
	pyautogui.click(x=1088, y=768)
	time.sleep(0.3)
	pyautogui.click(x=1461, y=466)
	time.sleep(0.1)
	pyautogui.click(x=1138, y=610)
	time.sleep(0.1)
	pyautogui.click(x=1222, y=331)
	time.sleep(1)
	wait_for_icon_to_appear('quests/no_more_quests.png')
	time.sleep(1)
	wait_for_icon_to_appear('quests/no_more_quests.png')
	time.sleep(1)
	wait_for_icon_to_appear('quests/no_more_quests.png')
	pyautogui.click(x=1207, y=254)
	time.sleep(0.1)
	pyautogui.click(x=1406, y=305)
	time.sleep(1)

# mysery_box

def mysery_box():
	time.sleep(1)
	pyautogui.click(x=1333, y=683)
	time.sleep(1)
	pyautogui.click(x=960, y=663)
	time.sleep(3)

# login gifts

def login_gifts():
	pyautogui.click(x=742, y=357)
	time.sleep(1)

	if pyautogui.locateOnScreen('events/login_gifts.png', confidence=0.8, grayscale=True):
		x, y = pyautogui.locateCenterOnScreen('events/login_gifts.png', confidence=0.8, grayscale=True)
		pyautogui.click(x=x, y=y)
		time.sleep(1)
		time.sleep(1)

		if pyautogui.locateOnScreen('events/claim_login_gifts.png', confidence=0.7, grayscale=True):
			x, y = pyautogui.locateCenterOnScreen('events/claim_login_gifts.png', confidence=0.7, grayscale=True)
			pyautogui.click(x=x, y=y)
		else:
			print('login gifts claim button no make sense')

		time.sleep(1)
		pyautogui.click(x=1406, y=304)
	else:
		print('login gifts event card not found')

	time.sleep(0.3)
	pyautogui.click(x=1406, y=304)
	time.sleep(1)

# emote

def emote():
	pyautogui.click(x=950, y=297)
	time.sleep(0.3)
	pyautogui.click(x=1158, y=762)
	time.sleep(0.3)
	pyautogui.click(x=965, y=656)
	time.sleep(0.3)
	pyautogui.click(x=1406, y=306)
	time.sleep(1)

# normal stuff

def routine():
	print('daily stuff...')
	login_wait()

	acc_num = accounts.index(start_with)

	for account in range(acc_num, len(accounts)):
		if account != accounts.index(start_with):
			switch_account(accounts[account])

		print('sweepin '+accounts[account]+'...')

		mysery_box()
		send_help()
		emote()
		login_gifts()
		send_help()
		quests()
		collect_gifts(accounts[account])
		send_help()
		time.sleep(0.3)

		acc_num += 1

	print('going back home...')
	switch_account('sneaky')

# shields all accounts

def shield():
	print('changing shields...')
	login_wait()

	acc_num = accounts.index(start_with)
	for account in accounts:
		if acc_num > 0:
			switch_account(account)

		print('bubblin '+account+' ...')
		time.sleep(3)
		pyautogui.click(x=1410, y=459)
		
		wait_for_icon_to_appear('boosts/shield.png')
		pyautogui.click('boosts/shield.png')
		time.sleep(3)

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
		
		time.sleep(3)
		pyautogui.click(x=1033, y=531)

		time.sleep(3)

		pyautogui.click(x=1404, y=306)
		time.sleep(3)

		evd = pyautogui.screenshot(region=(479, 269, 963, 543))
		evd.save(r'C:\Users\lawrencie\Desktop\reports\shield\\'+account+'.png')

		print('good, switching')
		acc_num += 1

	print('going back home...')
	switch_account('sneaky')

# prepares for kvk

def kvk_check():
	print('doing kvk...')
	login_wait()

	acc_num = accounts.index(start_with)

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
		acc_num = accounts.index(start_with)

		for account in accounts:
			if acc_num > 0:
				switch_account(account)
			print('sweepin '+account+'...')
			if runs == 0:
				pyautogui.click(x=744, y=359)

				while not pyautogui.locateOnScreen('rss/event_kvk.png', grayscale=True, confidence=0.8):
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

	acc_num = accounts.index(start_with)

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

	acc_num = accounts.index(start_with)

	for account in accounts:
		if acc_num > 0:
			switch_account(account)
		print('sweepin '+account+'...')

	print('do stuff here...')
	print('going back home...')
	switch_account('sneaky')

# testing

def say_start():
	print(start_with)
	print(accounts.index(start_with))
	time.sleep(8)

## procedure

lm_task = pyautogui.confirm(text='What you wanna do?', title='Task' , buttons=['routine', 'shield', 'kvk', 'dragon in', 'dragon out', 'cry'])

start_with = pyautogui.confirm(text='What you wanna do?', title='Task' , buttons=accounts)

cry()
open_game()

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
	say_start()
	print('More possibilities on the way ;)')

cry()

print('S: done')


