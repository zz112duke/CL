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
# include paths to bin in order to create a subject specific trial sequence
binDir = _thisDir + os.sep + u'bin'

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
    size=(1024, 768), fullscr=False, allowGUI=False,
    monitor='testMonitor', color=[1,1,1], useFBO=True)

##########Timer##########
globalClock = core.MonotonicClock() # to track the time since experiment started
trialClock = core.Clock() #unlike globalclock, gets reset each trial

Instr_1 = visual.TextStim(win=win, name='Instr_1 ', color='black',
    text ='hello')
Instr_2 = visual.TextStim(win=win, name='Instr_2 ', color='black',
    text ='now you are half way through')
Blank = visual.TextStim(win=win, name='blank', text='h', 
    font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=0, depth=0.0)

os.chdir(_thisDir + '/Stimuli_test')
Imagelist1 = list(os.listdir())
os.chdir(_thisDir)
Imagelist1 = [_thisDir + "/Stimuli_test/" + i for i in Imagelist1]

Image = visual.ImageStim(win=win, name='Image', 
    image= _thisDir + '/Stimuli_faces1/CK_f_01.jpg', mask=None,
    ori=0, pos=(0, 0), opacity=1, texRes=128, depth=0.0,
    size=(0.75, 1), interpolate = True)

duration = [2]*4
ITI = [2]*4
expmatrix = [Imagelist1, duration, ITI]
expmatrix = pd.DataFrame(expmatrix)
expmatrix = expmatrix.transpose()
expmatrix.columns = ['stim_image','Duration','ITI']

#####begin#####
Instr_1.setAutoDraw(True)

advance = 0
while advance < 1:
    if event.getKeys(keyList=["space"]):
        advance += 1
    if advance == 1:
        Instr_1.setAutoDraw(False)

    if event.getKeys(keyList=["escape"]):
        core.quit()
    win.flip()


theseKeys = []
trialcounter = 0
for trial in range(len(expmatrix)):
    t = 0
    overalltime = globalClock.getTime()
    trialClock.reset()  # clock
    continueRoutine = True

    ##------------------SET DURATION & ITI OF STIMULI-------------------##
    #duration 1000 ms
    duration = expmatrix.loc[trial,'Duration']
    
    #ITI jittering 800-2000 ms
    ITI = expmatrix.loc[trial,'ITI']

    ##---------------------SET STIMULI & RESPONSE---------------------------##
    stim_image = expmatrix.loc[trial,'stim_image']
    #print(stim_image)
    Image.setImage(stim_image)
    
    #doesn't show image6
    if trialcounter == 2:
        #instr_2 = trialClock.getTime()
        Instr_2.setAutoDraw(True)
        continueRoutine = True
        while continueRoutine:
            if event.getKeys(keyList=["escape"]):
                core.quit()
            if len(event.getKeys(keyList=["space"])) == 0:
                win.flip()
            else:
                break
        Instr_2.setAutoDraw(False)
        tinstr_2 = trialClock.getTime()
        #print(tinstr_2)
    else:
        pass


    ##--------------------------WHILE LOOP BEGINS-------------------------##
    while continueRoutine:
        if event.getKeys(keyList=["escape"]):
            core.quit()
        # get current time
        t = trialClock.getTime()
        key_resp = event.BuilderKeyResponse()

        ##--------------------STIMULI PRESENTATION-------------------------------##
        if trialcounter == 2:
            if t > tinstr_2 and t < ITI + tinstr_2:
                Blank.setAutoDraw(True)
            elif t > ITI + tinstr_2 and t < ITI + tinstr_2 + duration:
                Blank.setAutoDraw(False)
                Image.setAutoDraw(True)
            else:
                Blank.setAutoDraw(False)
                Image.setAutoDraw(False)
                continueRoutine = False
            
            theseKeys = event.getKeys(keyList=['w', 'o'])       
            if len(theseKeys) > 0 and trialClock.getTime() < ITI + duration:# at least one key was pressed
                if theseKeys[-1] != None:
                     key_resp.rt = key_resp.clock.getTime()
                     thisExp.addData('Response', theseKeys[-1])
                     thisExp.addData('RT', key_resp.rt)
                Image.setAutoDraw(False)
                Blank.setAutoDraw(False)
                continueRoutine = False


        else:
            if t < ITI:
                 Blank.setAutoDraw(True)
            elif t > ITI and t < ITI + duration:
                 Blank.setAutoDraw(False)
                 Image.setAutoDraw(True)
    
            else:
                 Image.setAutoDraw(False)
                 Blank.setAutoDraw(False)
                 continueRoutine = False
    

            theseKeys = event.getKeys(keyList=['w', 'o'])       
            if len(theseKeys) > 0 and trialClock.getTime() < ITI + duration:# at least one key was pressed
                if theseKeys[-1] != None:
                     key_resp.rt = key_resp.clock.getTime()
                     thisExp.addData('Response', theseKeys[-1])
                     thisExp.addData('RT', key_resp.rt)
                Image.setAutoDraw(False)
                Blank.setAutoDraw(False)
                continueRoutine = False
            
        if continueRoutine:
             win.flip()
        else:
             break
    
    trialcounter += 1
    thisExp.addData('Trial',trialcounter)
    thisExp.nextEntry()

    
    
    
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
    
    



