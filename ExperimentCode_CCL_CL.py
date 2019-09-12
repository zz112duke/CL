from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy.random import random, randint, normal, shuffle
import random
import os  # handy system and path functions
import sys  # to get file system encoding

import pandas as pd
import numpy as np
from operator import itemgetter 

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
current_working_directory = os.getcwd()

# Store info about the experiment session
expName = 'CCL_CL'  # from the Builder filename that created this script
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
    text='In this experiment, you will see a series of face images...Press w if the image shows a female face and o if it shows a male face...Press the spacebar to continue.')

Ending = visual.TextStim(win=win, name='Instr_1', color='black',
    text='Thank you for participating in this study. Press the spacebar to quit.')

##########Stimuli##########
os.chdir(current_working_directory + '/Stimuli_faces')
Imagelist = list(os.listdir())


Image = visual.ImageStim(win=win, name='Image', image='\\Users\\zz112\\Documents\\CCL\\Stimuli_faces\\CK_f_01.jpg', size=(0.42, 0.5), interpolate = True)
Blank = visual.TextStim(win=win, name='blank', text='hello', font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, color=u'black', colorSpace='rgb', opacity=1, depth=0.0);

##########Trial Sequence##########
trials = 240
duration = 3.0
ITI_min = 800.0
ITI_max = 2000.0
stim_image = []
corrAns = []
ITI = []



# index the images for high, medium and low frequencies for later selection
indices_all = (np.random.choice(len(Imagelist), 104, replace=False)).tolist()
indices_low = indices_all[:80]
indices_medium = indices_all[80:96]
indices_high = indices_all[96:104]

# select corresponding images
stim_image_high =list(itemgetter(*indices_high)(Imagelist))* 10
stim_image_medium = list(itemgetter(*indices_medium)(Imagelist))* 5
stim_image_low = list(itemgetter(*indices_low)(Imagelist))* 80
stim_image = stim_image_high +stim_image_medium + stim_image_low

# frequency
frequency = ['high']*80 + ['medium']*80 + ['low']*80

# corrAns
for i in stim_image:
    if ('m' or 'M') in i:
        corrAns.append('w')
    else:
        corrAns.append('o')


#ITI & duration
for i in range(240):
    ITI.append(random.randint(ITI_min, ITI_max)/1000)

duration = [duration]*240


expmatrix = [stim_image, frequency, corrAns, duration, ITI]




##----------------------------------------------------------------------------##
##-----------------------------START RUNNING----------------------------------##
##----------------------------------------------------------------------------##


##---------------------------START INSTRUCTIONS-------------------------------##

Instr_1.setAutoDraw(True)

advance = 0
while advance < 2:
    if event.getKeys(keyList=["space"]):
        advance += 1
    if advance == 1:
        Instr_1.setAutoDraw(False)
        Instr_2.setAutoDraw(True)
    else:
        Instr_2.setAutoDraw(False)

    if event.getKeys(keyList=["escape"]):
        core.quit()
    win.flip()


##------------------------------START TRIALS FOR LOOPS----------------------------------##

theseKeys = []
trialcounter = 0
for trial in range(len(stim_image)):
    t = 0
    overalltime = globalClock.getTime()
    trialClock.reset()  # clock
    continueRoutine = True

    ##------------------SET DURATION & ITI OF STIMULI-------------------##
    #duration 1000 ms
    duration = expmatrix[3][trial]
    
    #ITI jittering 800-2000 ms
    ITI = expmatrix[4][trial]

    ##---------------------SET STIMULI & RESPONSE---------------------------##
    Image.setImage(expmatrix[0][trial])
    stim_image = expmatrix[0][trial]
    frequency = expmatrix[1][trial]
    corrAns = expmatrix[2][trial]
    Blank.setAutoDraw(True)


    ##--------------------------WHILE LOOP BEGINS-------------------------##
    while continueRoutine:
        if event.getKeys(keyList=["escape"]):
            core.quit()
        # get current time
        t = trialClock.getTime()
        key_resp = event.BuilderKeyResponse()

        ##--------------------STIMULI PRESENTATION-------------------------------##
        
        if trialClock.getTime() < ITI:
             Blank.setAutoDraw(True)
        elif trialClock.getTime() > ITI and trialClock.getTime() < ITI + duration:
             Blank.setAutoDraw(False)
             Image.setAutoDraw(True)
        else:
             Image.setAutoDraw(False)
             continueRoutine = False


        theseKeys = event.getKeys(keyList=['w', 'o'])       
        if len(theseKeys) > 0 and trialClock.getTime() < ITI + duration:# at least one key was pressed
            if theseKeys[-1] != None:
                 key_resp.rt = key_resp.clock.getTime()
                 thisExp.addData('Response', theseKeys[-1])
                 thisExp.addData('RT', key_resp.rt)
        
            # was this 'correct'?
            if str(corrAns) in theseKeys:
                 key_resp.corr = 1
                 thisExp.addData('Accuracy', key_resp.corr)
            else:
                 key_resp.corr = 0
                 thisExp.addData('Accuracy', key_resp.corr)

            # a response ends the routine
            continueRoutine = False

    
        ##------------CHECK ALL IF COMPONENTS HAVE FINISHED---------------##

        if continueRoutine:
             win.flip()
        else:
             break
##--------------------------RECORD DATA-------------------------------##
    trialcounter += 1
    thisExp.addData('Trial',trialcounter)
    thisExp.addData('stim_image', stim_image)
    thisExp.addData('frequency', frequency)
    thisExp.addData('corrAns', corrAns) 
    thisExp.addData('duration', duration)    
    thisExp.addData('ITI', ITI)


    thisExp.nextEntry()


event.clearEvents(eventType='keyboard')
Ending.setAutoDraw(True)


while len(event.getKeys(keyList=["space"])) != 0:
     Ending.setAutoDraw(False)


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()