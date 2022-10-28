# do normal stuff
import pyautogui, time, os

class Turf():
	def __init__(self, app):
		self.app = app

	def shield(self):
		self.app.log.write('I: changing shields... \n\n')
		print('I: changing shields...')

		acc_num = self.app.accounts.index(self.app.start_with)

		for account in range(acc_num, len(self.app.accounts)):
			if account != self.app.accounts.index(self.app.start_with):
				self.switch_account(self.app.accounts[account])

			self.app.log.write('I: Bubblin '+self.app.accounts[account]+' ... \n\n')
			print('I: Bubblin '+self.app.accounts[account]+' ...')
			time.sleep(3)
			pyautogui.click(x=1410, y=459)
			
			self.app.guiman.wait_for_object('boosts/shield.png')
			x,y = pyautogui.locateCenterOnScreen('boosts/shield.png', confidence=0.8, grayscale=True)
			time.sleep(0.1)
			pyautogui.click(x=x, y=y)
			time.sleep(3)

			if self.shield_len == '8h':
			    # 8h
				pyautogui.click(x=1216, y=544)
			elif self.shield_len == '3d':
				# 3d
				pyautogui.click(x=1215, y=758)
			elif self.shield_len == '1d':
			    # 1d
				pyautogui.click(x=1225, y=649)
			else:
			    # 1d
				pyautogui.click(x=1225, y=649)
			
			time.sleep(3)
			pyautogui.click(x=1033, y=531)

			time.sleep(3)

			self.app.guiman.click_x()
			time.sleep(3)

			evd = pyautogui.screenshot(region=(479, 269, 963, 543))
			evd.save(os.environ['USERPROFILE']+'\\Desktop\\reports\\shield\\'+self.app.accounts[account]+'.png')

			self.app.log.write('I: Good, switching... \n\n')
			print('I: Good, switching')
			acc_num += 1

		self.app.log.write('I: Going back home... \n\n')
		print('I: Going back home...')
		self.switch_account('sneaky')

	def routine(self):

		self.app.log.write('I: Doing daily stuff... \n\n')
		print('I: Doing daily stuff...')

		accounts = self.app.accounts

		acc_num = accounts.index(self.app.start_with)

		for account in range(acc_num, len(accounts)):
			if account != accounts.index(self.app.start_with):
				self.switch_account(accounts[account])

			self.app.log.write('I: Sweepin '+accounts[account]+'... \n\n')
			print('I: Sweepin '+accounts[account]+'...')

			#self.project_track()
			self.mysery_box()
			self.send_help()
			self.emote()
			self.darknest()
			self.login_gifts()
			self.famskills()
			self.mysery_box()
			self.mall()
			self.sta(accounts[account])
			self.quests()
			self.collect_gifts(accounts[account])
			self.mysery_box()
			self.send_help()
			time.sleep(0.3)

			acc_num += 1

		self.app.log.write('I: Going back home... \n\n')
		print('I: Going back home...')
		self.switch_account('sneaky')

	def mysery_box(self):
		self.app.log.write('I: Opening mystery box... \n\n')
		print('I: Opening mystery box...')
		time.sleep(1)
		pyautogui.click(x=1333, y=683)
		time.sleep(1)
		pyautogui.click(x=960, y=663)
		time.sleep(3)
		self.app.guiman.click_x()

	def send_help(self):
		self.app.log.write('I: Sending help... \n\n')
		print('I: Sending help...')
		time.sleep(1)
		if pyautogui.locateOnScreen('turf/help.png', confidence=0.7):
			x,y = pyautogui.locateCenterOnScreen('turf/help.png', confidence=0.7)
			pyautogui.click(x=x, y=y)
			time.sleep(1)
			pyautogui.click(x=955, y=766)
			time.sleep(1)
		
		self.app.guiman.click_x()

	def emote(self):
		self.app.log.write('I: Emoting... \n\n')
		print('I: Emoting...')
		pyautogui.click(x=950, y=297)
		time.sleep(0.3)
		pyautogui.click(x=1158, y=762)
		time.sleep(0.3)
		pyautogui.click(x=965, y=656)
		time.sleep(0.3)
		self.app.guiman.click_x()
		time.sleep(1)

	def darknest(self):
		self.app.log.write('I: Collecting essence rewards... \n\n')
		print('I: Collecting essence rewards...')
		time.sleep(1)
		if pyautogui.locateOnScreen('projects/tick.png', confidence=0.7, grayscale=True):
			x,y = pyautogui.locateCenterOnScreen('projects/tick.png', confidence=0.7, grayscale=True)
			pyautogui.click(x=x, y=y)
			time.sleep(1)

			if pyautogui.locateOnScreen('lab/collect.png', confidence=0.7, grayscale=True):
				x,y = pyautogui.locateCenterOnScreen('lab/collect.png', confidence=0.7, grayscale=True)
				pyautogui.click(x=x, y=y)
				time.sleep(0.3)

				self.app.guiman.wait_for_object('lab/ok_collect_ess.png')
				x,y = pyautogui.locateCenterOnScreen('lab/ok_collect_ess.png', confidence=0.7, grayscale=True)
				pyautogui.click(x=x, y=y)
				time.sleep(1)

				if pyautogui.locateOnScreen('lab/transmute.png', confidence=0.7, grayscale=True):
					x,y = pyautogui.locateCenterOnScreen('lab/transmute.png', confidence=0.7, grayscale=True)
					pyautogui.click(x=x, y=y+50)
					time.sleep(0.3)
					pyautogui.click(x=961, y=676)
					time.sleep(1)
				else:
					self.app.log.write('W: No essence to transmute... \n\n')
					print('W: No essence to transmute')

			else:
				self.app.log.write('E: No essence to collect, weird... \n\n')
				print('E: No essence to collect, weird...')

			self.app.guiman.click_x()
		else:
			self.app.log.write('I: No essence, will do this part in turf explore...\n\n')
			print('I: No essence, will do this part in turf explore...')

	def login_gifts(self):
		self.app.log.write('I: Collecting login gifts... \n\n')
		print('I: Collecting login gifts...')
		pyautogui.click(x=742, y=357)
		time.sleep(1)
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
				self.app.log.write('E: Login gifts claim button no make sense... \n\n')
				print('E: Login gifts claim button no make sense')

			time.sleep(1)
		else:
			self.app.log.write('W: Login gifts event card not found... \n\n')
			print('W: Login gifts event card not found')

		time.sleep(0.3)
		self.app.guiman.click_x()
		time.sleep(1)

	def sta(self, account):
		self.app.log.write('I: Using sta... \n\n')
		print('I: Using sta... ')
		hero = self.app.guide['accounts'][account]['hero']
		stage_type = self.app.guide['accounts'][account]['sta']
		max_scrls = 10

		time.sleep(0.3)
		pyautogui.click(x=1326, y=777)
		time.sleep(0.3)
		pyautogui.moveTo(x=1120, y=676)

		while not pyautogui.locateOnScreen('heroes/'+hero+'.png', grayscale=True, confidence=0.7) and max_scrls > 0:
		    pyautogui.drag(0, -100, 1)
		    pyautogui.move(0, 100)
		    max_scrls -= 1

		if pyautogui.locateOnScreen('heroes/'+hero+'.png', grayscale=True, confidence=0.7):
			x,y = pyautogui.locateCenterOnScreen('heroes/'+hero+'.png', grayscale=True, confidence=0.7)
			pyautogui.click(x=x, y=y)
			time.sleep(0.5)

			evd = pyautogui.screenshot(region=(479, 269, 963, 543))
			evd.save(os.environ['USERPROFILE']+'\\Desktop\\reports\\heroes\\'+account+'.png')

			if stage_type == 'elite':
				time.sleep(0.1)
				pyautogui.click(x=1283, y=723)
				time.sleep(1)
				pyautogui.click(x=849, y=525)
				time.sleep(0.4)

				if pyautogui.locateOnScreen('heroes/fight.png', grayscale=True, confidence=0.7):
					pyautogui.click(x=1322, y=563)
					time.sleep(0.1)
					pyautogui.click(x=1322, y=563)
					time.sleep(0.1)
					pyautogui.click(x=1322, y=563)

				else:
					self.app.log.write('E: No fight button? how? moving on... \n\n')
					print('E: No fight button? how? moving on...')

			elif stage_type == 'normal':
				if pyautogui.locateOnScreen('heroes/none.png', grayscale=True, confidence=0.7):
					x,y = pyautogui.locateCenterOnScreen('heroes/none.png', grayscale=True, confidence=0.7)
					pyautogui.click(x=x, y=y)
					time.sleep(1)
					pyautogui.click(x=1118, y=617)
					time.sleep(1)

					sink_hole = 5
					while not pyautogui.locateOnScreen('heroes/obtained_from.png', grayscale=True, confidence=0.7):
						pyautogui.click(x=945, y=587)
						sink_hole -= 1
						time.sleep(0.8)

					if pyautogui.locateOnScreen('heroes/obtained_from.png', grayscale=True, confidence=0.7):
						pyautogui.click(x=814, y=647)
						time.sleep(1)
						pyautogui.click(x=1322, y=563)
						time.sleep(0.1)
						pyautogui.click(x=1322, y=563)
						time.sleep(0.1)
						pyautogui.click(x=1322, y=563)

					else:
						self.app.log.write('E: Sink hole too deep... \n\n')
						print('E: Sink hole too deep...')

			else:
				self.app.log.write('E: Type not defined, moving on... \n\n')
				print('E: Type not defined, moving on...')

		else:
			self.app.log.write('E: Hero not found, strange, moving on... \n\n')
			print('E: Hero not found, strange, moving on...')

		time.sleep(1)
		self.app.guiman.click_x()

	def quests(self):
		self.app.log.write('I: Sweeping quests... \n\n')
		print('I: Sweeping quests...')
		time.sleep(1)
		pyautogui.click(x=1088, y=768)
		time.sleep(0.3)
		pyautogui.click(x=1461, y=465)
		time.sleep(0.1)
		pyautogui.click(x=1139, y=600)
		time.sleep(0.1)
		pyautogui.click(x=1220, y=335)
		time.sleep(1)
		self.app.guiman.wait_for_object('quests/no_more_quests.png')
		time.sleep(1)
		self.app.guiman.wait_for_object('quests/no_more_quests.png')
		time.sleep(1)
		self.app.guiman.wait_for_object('quests/no_more_quests.png')
		pyautogui.click(x=1210, y=248)
		time.sleep(0.1)
		#tr q
		pyautogui.click(x=1295, y=383)
		time.sleep(0.3)

		self.app.log.write('I: Collecting treasure quest... \n\n')
		print('I: Collecting treasure quest...')

		if pyautogui.locateOnScreen('quests/t_quest.png', confidence=0.7, grayscale=True):
			x,y = pyautogui.locateCenterOnScreen('quests/t_quest.png', confidence=0.7, grayscale=True)
			pyautogui.click(x=x, y=y)
			time.sleep(1)
		else:
			self.app.log.write('No tq to collect... \n\n')
			print('No tq to collect...')
		# dq
		pyautogui.click(x=623, y=383)
		time.sleep(0.7)

		self.app.log.write('I: Collecting dq... \n\n')
		print('I: Collecting dq...')

		if pyautogui.locateOnScreen('quests/collect.png', confidence=0.7, grayscale=True):
			while pyautogui.locateOnScreen('quests/collect.png', confidence=0.7, grayscale=True):
				try:
					x,y = pyautogui.locateCenterOnScreen('quests/collect.png', confidence=0.7, grayscale=True)
					pyautogui.click(x=x, y=y)
				except TypeError:
					self.app.alerts.cry()
				
		else:
			self.app.log.write('I: No dq to collect... \n\n')
			print('I: No dq to collect...')

		self.app.guiman.click_x()
		time.sleep(1)

	def collect_gifts(self, account):
		self.app.log.write('I: Collecting gifts... \n\n')
		print('I: Collecting gifts...')
		time.sleep(0.3)
		pyautogui.click(x=927, y=775)
		time.sleep(3)
		pyautogui.click(x=1370, y=412)
		time.sleep(1)
		pyautogui.click(x=1206, y=481)
		time.sleep(1.9)
		pyautogui.click(x=1235, y=454)
		time.sleep(1)

		if self.app.guide['accounts'][account]['vip']:
			self.app.guiman.wait_for_object('guild/open_all_gifts.png')
			x, y = pyautogui.locateCenterOnScreen('guild/open_all_gifts.png', confidence=0.8, grayscale=True)
			pyautogui.click(x=x, y=y)
			time.sleep(3)
			x, y = pyautogui.locateCenterOnScreen('guild/delete_all.png', confidence=0.8, grayscale=True)
			pyautogui.click(x=x, y=y)
			self.app.guiman.wait_for_object('guild/no_bonus_chests.png')
			time.sleep(1)
			pyautogui.click(x=979, y=449)
			self.app.guiman.wait_till_gone('guild/no_bonus_chests.png')
			time.sleep(3)
			self.app.guiman.wait_for_object('guild/open_all_gifts.png')
			x, y = pyautogui.locateCenterOnScreen('guild/open_all_gifts.png', confidence=0.8, grayscale=True)
			pyautogui.click(x=x, y=y)
			time.sleep(3)
			x, y = pyautogui.locateCenterOnScreen('guild/delete_all.png', confidence=0.8, grayscale=True)
			pyautogui.click(x=x, y=y)
			self.app.guiman.wait_for_object('guild/no_guild_gifts.png')

		else:
			pyautogui.click(x=1463, y=467)
			time.sleep(1)
			pyautogui.click(x=1137, y=457)
			time.sleep(1)
			pyautogui.click(x=1221, y=332)
			self.app.guiman.wait_for_object('guild/no_bonus_chests.png')
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
			self.app.guiman.wait_for_object('guild/no_guild_gifts.png')
			pyautogui.click(x=1207, y=254)

		self.app.guiman.click_x()
		time.sleep(3)
		evd = pyautogui.screenshot(region=(479, 269, 963, 543))
		evd.save(r'C:\Users\PEPPA\Desktop\reports\guild\\'+account+'.png')

	def send_help(self):
		self.app.log.write('I: Sending help... \n\n')
		print('I: Sending help...')
		time.sleep(1)
		if pyautogui.locateOnScreen('turf/help.png', confidence=0.7):
			x,y = pyautogui.locateCenterOnScreen('turf/help.png', confidence=0.7)
			pyautogui.click(x=x, y=y)
			time.sleep(1)
			pyautogui.click(x=955, y=766)
			time.sleep(1)
		
		self.app.guiman.click_x()

	def project_track(self):
		pass

	def mall(self):
		print('I: Opening mall chest...')
		self.app.log.write('I: Opening mall chest... \n\n')
		pyautogui.click(x=886, y=346)
		time.sleep(3)
		pyautogui.click(x=546, y=592)

		self.app.guiman.click_x()

	def famskills(self):
		self.app.log.write('I: Using familiar skill... \n\n')
		print('I: Using familiar skill...')
		pyautogui.click(x=1385, y=528)
		time.sleep(0.3)

		max_scrls = 10
		pyautogui.moveTo(x=1120, y=676)
		pyautogui.drag(0, 100, 0.3)
		pyautogui.move(0, -100)
		time.sleep(3)

		while not pyautogui.locateOnScreen('familiar/refreshed.png', grayscale=True, confidence=0.8) and max_scrls > 0:
		    pyautogui.drag(0, -100, 1)
		    pyautogui.move(0, 100)
		    max_scrls -= 1

		if pyautogui.locateOnScreen('familiar/refreshed.png', grayscale=True, confidence=0.8):
			x,y = pyautogui.locateCenterOnScreen('familiar/refreshed.png', grayscale=True, confidence=0.8)
			pyautogui.click(x=x+619, y=y)
			time.sleep(0.5)
		else:
			self.app.log.write('E: Skill not found... \n\n')
			print('E: Skill not found...')

		self.app.guiman.click_x()

	def shelter(self):
		self.app.guiman.click_x()

	def switch_account(self, account):
		self.app.log.write('I: Switching to '+account+'... \n\n')
		print('I: Switching to '+account+' ...')
		pyautogui.click(x=1170, y=773)
		time.sleep(0.4)
		pyautogui.click(x=725, y=441)
		time.sleep(0.4)
		pyautogui.click(x=953, y=574)
		time.sleep(0.4)
		pyautogui.click(x=981, y=518)
		self.app.guiman.wait_for_object('accounts/'+account+'.png', 10)
		time.sleep(0.1)
		pyautogui.click('accounts/'+account+'.png')
		time.sleep(0.3)
		pyautogui.click('accounts/ok_switch_account.png')
		time.sleep(1)
		self.app.guiman.wait_for_object('accounts/confirm_switch.png', 10)
		time.sleep(1)
		x, y = pyautogui.locateCenterOnScreen('accounts/confirm_switch.png', confidence=0.8, grayscale=True)
		time.sleep(0.3)
		pyautogui.click(x=x, y=y)
		time.sleep(8)
		self.app.login_wait()
