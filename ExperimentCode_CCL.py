from psychopy import locale_setup, gui, visual, core, data, event, logging
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy.random import random, randint, normal, shuffle
import random
import os  # handy system and path functions
import sys  # to get file system encoding

import pandas as pd
import numpy as np

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)
current_working_directory = os.getcwd()

# Store info about the experiment session
expName = 'CCL'  # from the Builder filename that created this script
expInfo = {'participant':'','session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel during popout
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, "ses_" + expInfo['session'])


# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file


# Setup the Window
win = visual.Window(
    size=(960, 400), fullscr=False, allowGUI=False,
    monitor='testMonitor', color=[1,1,1], useFBO=True)

###Stimuli###
os.chdir(current_working_directory + '/Stimuli_faces')
Imagelist = os.listdir()
print (Imagelist)

Image = visual.ImageStim(win=win, name='Image', image=Image_present, size=(0.42, 0.5), interpolate = True)


###Trial Sequence###
trials = 240
def expsequence():
    stim_image = np.random.shuffle(Imagelist)
    frequency = np.random.shuffle(['high']*80 + ['medium']*80 + ['low']*80)
    print (frequency)
    
    corrAns = []
    duration = []
    ITI = []
    
    for i in stim_image:
        if i #start with female:
            corrAns.append('q')
        else:
            corrAns.append('p')
    
    ITI = 
    







