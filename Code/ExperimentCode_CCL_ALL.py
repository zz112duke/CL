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



##########Version##########
# version 1 [non,con] version 2 [con,non]
version = random.choice([1,2])
print (version)


##########Stimuli##########
Imagelist1 = list(os.listdir(_thisDir + '/Set1'))
Imagelist1 = ["Set1/" + i for i in Imagelist1]

Imagelist2 = list(os.listdir(_thisDir + '/Set2'))
Imagelist2 = ["Set2/" + i for i in Imagelist2]

Practicelist = list(os.listdir(_thisDir + '/Practice'))


Image = visual.ImageStim(win=win, name='Image', 
    image= _thisDir + '/Set1/CK_f_01.jpg', mask=None,
    ori=0, pos=(0, 0), opacity=1, texRes=128, depth=0,
    size=(0.75, 1), interpolate = True)

stroop_text =visual.TextStim(win=win, name='stroop_text',
    text='default',font=u'Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color=u'red', colorSpace='rgb', opacity=1,
    depth=0)

Blank = visual.TextStim(win=win, name='blank', text='h', 
    font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=0, depth=0.0)

Ending = visual.TextStim(win=win, name='Instr_1', color='black',
    text='Thank you for participating in this study. Press the spacebar to quit and call over the researcher for a post-task.')

###Indexing Image###
# index the images for high, medium and low frequencies for later selection
#indices_all = (np.random.choice(len(Imagelist), 104, replace=False)).tolist()
indices_all = list(range(104))
indices_low = indices_all[:80]
indices_medium = indices_all[80:96]
indices_high = indices_all[96:104]

# select corresponding images
random.shuffle(Imagelist1)
stim_image_high1 = [Imagelist1[i] for i in indices_high]*10
stim_image_medium1 = [Imagelist1[i] for i in indices_medium]*5
stim_image_low1 = [Imagelist1[i] for i in indices_low]
stim_image1 = stim_image_high1 +stim_image_medium1 + stim_image_low1

random.shuffle(Imagelist2)
stim_image_high2 = [Imagelist2[i] for i in indices_high]*10
stim_image_medium2 = [Imagelist2[i] for i in indices_medium]*5
stim_image_low2 = [Imagelist2[i] for i in indices_low]
stim_image2 = stim_image_high2 +stim_image_medium2 + stim_image_low2

##########Timing##########
trials = 240
duration = 1.0
ITI_min = 800.0
ITI_max = 2000.0

ITI = []
#ITI & duration
for i in range(240):
    ITI.append(random.randint(ITI_min, ITI_max)/1000)

duration = [duration]*240


##########Frequency##########
frequency = ['high']*80 + ['medium']*80 + ['low']*80

##########Congruency##########
congruency_con = ['con']*40 + ['incon']*40 + ['con']*40 + ['incon']*40 + ['con']*40 + ['incon']*40
congruency_non = ['N/A']*240


image_set = [stim_image1,stim_image2]
random.shuffle(image_set)

##########corrAns##########
# S-R mapping is different from exp version so needs a new number generator #
# 0 --> female w, male o; 1 --> female o, male w
Ans_version = random.choice([0,1])

corrAns1 = []
corrAns2 = []

if Ans_version==0:
    SR = ['w','o']
    for i in image_set[0]:
        if ('m' or 'M') in i:
            corrAns1.append(SR[1])
        else:
            corrAns1.append(SR[0])
    for i in image_set[1]:
        if ('m' or 'M') in i:
            corrAns2.append(SR[1])
        else:
            corrAns2.append(SR[0])
else:
    SR = ['o','w']
    for i in image_set[0]:
        if ('m' or 'M') in i:
            corrAns1.append(SR[1])
        else:
            corrAns1.append(SR[0])
    for i in image_set[1]:
        if ('m' or 'M') in i:
            corrAns2.append(SR[1])
        else:
            corrAns2.append(SR[0])



##########Exp Matrix##########
#Turn Exp Matrix into df to randomize rows
expmatrix_non = [image_set[0], frequency, congruency_non, corrAns1, duration, ITI]
expmatrix_non = pd.DataFrame(expmatrix_non)
expmatrix_non = expmatrix_non.transpose()
expmatrix_non.columns = ['stim_image','Frequency','Congruency','corrAns','Duration','ITI']
expmatrix_non = expmatrix_non.sample(frac=1).reset_index(drop=True)

expmatrix_con = [image_set[1], frequency, congruency_con, corrAns2, duration, ITI]
expmatrix_con = pd.DataFrame(expmatrix_con)
expmatrix_con = expmatrix_con.transpose()
expmatrix_con.columns = ['stim_image','Frequency','Congruency','corrAns','Duration','ITI']
expmatrix_con = expmatrix_con.sample(frac=1).reset_index(drop=True)



if version == 1:
    expmatrix = pd.concat([expmatrix_non , expmatrix_con],ignore_index=True)
else:
    expmatrix = pd.concat([expmatrix_con , expmatrix_non],ignore_index=True)

#Practice Matrix






##########Instruction##########

# Beginning Instr
lines_begin = [line.rstrip('\n') for line in open(os.path.join(binDir, "CLInstr_Begin.txt"))]
if version == 2:
    lines_begin.append('A word will also be presented on top of every face image. \nYour task is to ignore the meaning of the word and still to categorize the gender of the face image.')
else:
    pass


if Ans_version == 0:
    lines_begin.append('Press' + ' ' + SR[0] + ' ' + 'if the image shows a female face and' + ' ' + SR[1] + ' '+ 'if it shows a male face.')
else:
    lines_begin.append('Press' + ' ' + SR[0] + ' ' + 'if the image shows a male face and' + ' ' + SR[1] + ' ' + 'if it shows a female face.')
lines_begin.append("Memorize that task rule and press the space bar to begin.")

# Mid-way Instr (task change)
lines_mid = [line.rstrip('\n') for line in open(os.path.join(binDir, "CLInstr_Mid.txt"))]
if version == 1:
    lines_mid.append('This time, a word will be presented on top of every face image.\nYour task is to ignore the meaning of the word and still to categorize the gender of the face image')
else:
    lines_mid.append('This time, the word will no longer be shown on top of the images. \nYour task is still to categorize the face image.')
lines_mid.append("Please memorize the task rule and press the space bar to begin.")

# Practice Instr
lines_practice = [line.rstrip('\n') for line in open(os.path.join(binDir, "CLInstr_Practice.txt"))]
lines_practice.append

Instr_1 = visual.TextStim(win=win, name='Instr_1 ', color='black',
    text=(' '.join(map(str, lines_begin))))
Instr_2 = visual.TextStim(win=win, name='Instr_2 ', color='black',
    text=(' '.join(map(str, lines_mid))))
Instr_Practice = visual.TextStim(win=win, name='Instr_Practice', color='black',
    text=(' '.join(map(str, lines_practice))))




##----------------------------------------------------------------------------##
##-----------------------------START RUNNING----------------------------------##
##----------------------------------------------------------------------------##


##---------------------------START INSTRUCTIONS-------------------------------##
# Should set the ins according to the version
Instr_1.setAutoDraw(True)

advance = 0
while advance < 2:
    if event.getKeys(keyList=["space"]):
        advance += 1
    if event.getKeys(keyList=["space"]):
        advance += 2
        Instr_1.setAutoDraw(False)
        Instr_Practice.setAutoDraw(True)
    if advance == 2:
        Instr_Practice.setAutoDraw(False)

    if event.getKeys(keyList=["escape"]):
        core.quit()
    win.flip()

##---------------------------START Practice-------------------------------## 
theseKeys = []
for ptrial in range(len(Practicelist)):
    t = 0
    trialClock.reset()
    continueRoutine = True
    



##------------------------------START THE EXPERIMENT----------------------------------##
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
    Image.setImage(stim_image)
    frequency = expmatrix.loc[trial,'Frequency']
    corrAns = expmatrix.loc[trial,'corrAns']
    congruency = expmatrix.loc[trial,'Congruency']
    
    if congruency != 'N/A':
        if congruency == 'con':
            if ('m' or 'M') in stim_image:
                 stroop_text.setText('Male')
            else:
                 stroop_text.setText('Female')
        else:
            if ('m' or 'M') in stim_image:
                 stroop_text.setText('Female')
            else:
                 stroop_text.setText('Male')
    else:
         pass


    if trialcounter == 240:
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
        if trialcounter == 240:
            if t > tinstr_2 and t < ITI + tinstr_2:
                Blank.setAutoDraw(True)
            elif t > ITI + tinstr_2 and t < ITI + tinstr_2 + duration:
                Blank.setAutoDraw(False)
                Image.setAutoDraw(True)
                if congruency != 'N/A':
                    stroop_text.setAutoDraw(True)
                else:
                    pass
            else:
                Image.setAutoDraw(False)
                Blank.setAutoDraw(False)
                if congruency != 'N/A':
                    stroop_text.setAutoDraw(False)
                else:
                    pass
                continueRoutine = False
                
            theseKeys = event.getKeys(keyList=['w', 'o'])
            if len(theseKeys) == 0:
                 key_resp.corr = 0
                 thisExp.addData('Accuracy', key_resp.corr)
            if len(theseKeys) > 0 and trialClock.getTime() < ITI + tinstr_2 + duration:# at least one key was pressed
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

        else:
            if t < ITI:
                 Blank.setAutoDraw(True)
            elif t > ITI and t < ITI + duration:
                 Blank.setAutoDraw(False)
                 Image.setAutoDraw(True)
                 if congruency != 'N/A':
                     stroop_text.setAutoDraw(True)
                 else:
                     pass
    
            else:
                 Image.setAutoDraw(False)
                 Blank.setAutoDraw(False)
                 if congruency != 'N/A':
                     stroop_text.setAutoDraw(False)
                 else:
                     pass
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
    thisExp.addData('congruency', congruency) 
    thisExp.addData('text', stroop_text.text)
    thisExp.addData('corrAns', corrAns) 
    thisExp.addData('duration', duration)    
    thisExp.addData('ITI', ITI)
        
    thisExp.nextEntry()

#read the exp matrix, read the low frequency especially, since they'll be in every pair.








event.clearEvents(eventType='keyboard')
Ending.setAutoDraw(True)


if len(event.getKeys(keyList=["space"])) != 0:
     Ending.setAutoDraw(False)


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()