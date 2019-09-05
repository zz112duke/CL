from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy.random import random, randint, normal, shuffle
import random
import os  # handy system and path functions
import sys  # to get file system encoding

import pandas as pd
import numpy as np

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
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

##########Timer##########
globalClock = core.MonotonicClock() # to track the time since experiment started
trialClock = core.Clock() #unlike globalclock, gets reset each trial



##########Instruction##########
Instr_1 = visual.TextStim(win=win, name='Instr_1', color='black',
    text='Please read these instructions carefully before you begin the experiment. Press the spacebar to continue.')

Instr_2 = visual.TextStim(win=win, name='Instr_2', color='black',
    text='In this experiment, you will see a series of face images...Press q if it is a female face and p if it is a male face...')



##########Stimuli##########
os.chdir(current_working_directory + '/Stimuli_faces')
Imagelist = list(os.listdir())
print(Imagelist)


#Image = visual.ImageStim(win=win, name='Image', image=stim_image, size=(0.42, 0.5), interpolate = True)


##########Trial Sequence##########
trials = 240
duration = 1000
ITI_min = 800
ITI_max = 2000
stim_image = []
corrAns = []
ITI = []


Imagelist = np.random.shuffle(Imagelist)
stim_image.append(list(np.random.choice(Imagelist, 8, replace=False)) * 80)
stim_image.append(list(np.random.choice(Imagelist, 16, replace=False)) * 80)
stim_image.append(list(np.random.choice(Imagelist, 80, replace=False)) * 80)

frequency = np.random.shuffle(['high']*80 + ['medium']*80 + ['low']*80)
print (frequency)
    
#    
#    for i in stim_image:
#        if i #start with female:
#            corrAns.append('q')
#        else:
#            corrAns.append('p')
#    
ITI = ITI.append(random.randint(ITI_min, ITI_max))
duration = [duration]*240

#print([stim_image, frequency, corrAns, duration, ITI])
print([stim_image, frequency, duration, ITI])


##----------------------------------------------------------------------------##
##--------------------------START RUNNING TRIALS------------------------------##
##----------------------------------------------------------------------------##


##---------------------------START INSTRUCTIONS-------------------------------##

Instr_1.setAutoDraw(True)

advance = 0
while advance < 10:
    if event.getKeys(keyList=["space"]):
        advance += 1
    if advance == 1:
        Instr_1.setAutoDraw(False)
        Instr_2.setAutoDraw(True)
#    elif advance == 2:
#        Instr_2.setAutoDraw(False)
#        Instr_3.setAutoDraw(True)
#     
    if event.getKeys(keyList=["escape"]):
        core.quit()
    win.flip()










