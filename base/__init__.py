## imports

import subprocess, json, os
from datetime import datetime
from base.main import MiApp
from base.alerts import Alerts
from base.ui import MiGui
from base.maintenance import Turf

# Init app
app = MiApp()

# Start Rog
subprocess.Popen('C:\\LDPlayer\\LDPlayer4.0\\dnplayer.exe')

# Open log channel
ts = datetime.now()
trr = os.environ['USERPROFILE']+'\\Desktop\\reports\\logs\\'+str(ts.day)+'-'+str(ts.month)+' '+str(ts.hour)+str(ts.minute)+' log.txt'
app.log = open(trr, 'w')

# Open alert channel
app.alerts = Alerts()

# Pull json settings
guide_json = open('guide.json')
guide = json.load(guide_json)
app.accounts = [*guide['accounts'].keys()]
app.guide = guide

# Load gui machine
app.guiman = MiGui(app)

# Load turf tasks
app.turf = Turf(app)
