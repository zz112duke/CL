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
    size=(1024, 768), fullscr=True, allowGUI=False,
    monitor='testMonitor', color=[1,1,1], useFBO=True)

##########Timer##########
globalClock = core.MonotonicClock() # to track the time since experiment started
Practice_1_Clock = core.Clock() #unlike globalclock, gets reset each trial
Practice_2_Clock = core.Clock()
Task_1_Clock = core.Clock()
Task_2_Clock = core.Clock()

##########Version##########
# version 1 [non,con] version 2 [con,non]
version = random.choice([1,2])
print(version)

##########Stimuli##########
Imagelist1 = list(os.listdir(_thisDir + '/Set1'))
Imagelist1 = ["Set1/" + i for i in Imagelist1]
print(Imagelist1)

Imagelist2 = list(os.listdir(_thisDir + '/Set2'))
Imagelist2 = ["Set2/" + i for i in Imagelist2]
print(Imagelist2)

Practicelist = list(os.listdir(_thisDir + '/Practice'))
Practicelist = ["Practice/" + i for i in Practicelist]

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

Correct =visual.TextStim(win=win, name='Correct',
    text='Correct',font=u'Arial',
    pos=(0, -0.75), height=0.2, wrapWidth=None, ori=0, 
    color=u'red', colorSpace='rgb', opacity=1,
    depth=0)

Incorrect =visual.TextStim(win=win, name='Incorrect',
    text='Incorrect',font=u'Arial',
    pos=(0, -0.75), height=0.2, wrapWidth=None, ori=0, 
    color=u'red', colorSpace='rgb', opacity=1,
    depth=0)

Post_Q1 = visual.TextStim(win=win, name='blank', text='Have you noticed that some face images were presented with different frequencies \ (i.e. some showed up more times than the others)? \ Press' + 'y' + 'if you noticed and' + 'n' + 'if you did not', 
    font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1, depth=0.0)

Instr_Post = visual.TextStim(win=win, name='blank', text='Now you will be presented with images that you have seen in the main experiment. Indicate which one you think was presented in the main experiment more frequently by clicking on the image. Press the space bar to contiune. ', 
    font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1, depth=0.0)

stim_image_post = visual.ImageStim(win=win, name='Image', 
    image= _thisDir + '/Set1/CK_f_01.jpg', mask=None,
    ori=0, pos=(0, 0), opacity=1, texRes=128, depth=0,
    size=(0.75, 1), interpolate = True)

Post_Q2 =visual.TextStim(win=win, name='Post_Q2',
    text='Which one was presented higher or lower frequency in the main experiment?',font=u'Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color=u'red', colorSpace='rgb', opacity=1,
    depth=0)


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
stim_image1 = Practicelist*3 + stim_image_high1 +stim_image_medium1 + stim_image_low1
print(stim_image1)

random.shuffle(Imagelist2)
stim_image_high2 = [Imagelist2[i] for i in indices_high]*10
stim_image_medium2 = [Imagelist2[i] for i in indices_medium]*5
stim_image_low2 = [Imagelist2[i] for i in indices_low]
stim_image2 = Practicelist*3 + stim_image_high2 +stim_image_medium2 + stim_image_low2
print (stim_image2)

##########Timing##########
trials = 240
duration = 1.0
ITI_min = 800.0
ITI_max = 2000.0

ITI = []
#ITI & duration
for i in range(252):
    ITI.append(random.randint(ITI_min, ITI_max)/1000)

duration = [duration]*252


##########Frequency##########
frequency = ['None']*12 + ['high']*80 + ['medium']*80 + ['low']*80

##########Congruency##########
congruency_con = ['con']*6 + ['incon']*6 + ['con']*40 + ['incon']*40 + ['con']*40 + ['incon']*40 + ['con']*40 + ['incon']*40
#congruency_con_practice = ['con']*6 + ['incon']*6
congruency_non = ['None']*252


image_set = [stim_image1,stim_image2]
random.shuffle(image_set)

##########corrAns##########
# S-R mapping is different from exp version so needs a new number generator #
# 0 --> female w, male o; 1 --> female o, male w
Ans_version = random.choice([0,1])
print(Ans_version)

corrAns1 = []
corrAns2 = []

if Ans_version==0:
    SR = ['w','o']
    for i in image_set[0]:
        if ('m' or  'M') in i:
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
expmatrix_non_exp = expmatrix_non[12:252].sample(frac=1).reset_index(drop=True)
expmatrix_non_prac = expmatrix_non[0:12].sample(frac=1).reset_index(drop=True)

expmatrix_con = [image_set[1], frequency, congruency_con, corrAns2, duration, ITI]
expmatrix_con = pd.DataFrame(expmatrix_con)
expmatrix_con = expmatrix_con.transpose()
expmatrix_con.columns = ['stim_image','Frequency','Congruency','corrAns','Duration','ITI']
expmatrix_con_exp = expmatrix_con[12:252].sample(frac=1).reset_index(drop=True)
expmatrix_con_prac = expmatrix_con[0:12].sample(frac=1).reset_index(drop=True)


if version == 1:
    expmatrix = pd.concat([expmatrix_non_prac , expmatrix_non_exp, expmatrix_con_prac, expmatrix_con_exp],ignore_index=True)
else:
    expmatrix = pd.concat([expmatrix_con_prac, expmatrix_con_exp, expmatrix_non_prac , expmatrix_non_exp],ignore_index=True)

expmatrix.to_csv(r'expmatrix.csv')
##########Instruction##########
# Beginning Instr
lines_begin_1 = [line.rstrip('\n') for line in open(os.path.join(binDir, "CLInstr_Begin1.txt"))]
if version == 2:
    lines_begin_1.append('A text label will also be presented on top of every face image.')
else:
    pass

lines_begin_2 = [line.rstrip('\n') for line in open(os.path.join(binDir, "CLInstr_Begin2.txt"))]
if version == 2:
    lines_begin_2.append('ignore the meaning of the word and to categorize the gender of the face image.')
else:
    lines_begin_2.append('categorize the gender of the face image.')
if Ans_version == 0:
    lines_begin_2.append('Press' + ' ' + SR[0] + ' ' + 'if the image shows a female face and' + ' ' + SR[1] + ' '+ 'if it shows a male face.')
else:
    lines_begin_2.append('Press' + ' ' + SR[0] + ' ' + 'if the image shows a male face and' + ' ' + SR[1] + ' ' + 'if it shows a female face.')
lines_begin_2.append("Memorize that task rule and press the space bar to begin the practice trials.")

# Mid-way Instr (task change)
lines_mid_1 = [line.rstrip('\n') for line in open(os.path.join(binDir, "CLInstr_Mid.txt"))]
if version == 1:
    lines_mid_1.append('This time, a text label will be presented on top of every face image.')
else:
    lines_mid_1.append('This time, the word will no longer be shown on top of the images.')

lines_mid_2 = [line.rstrip('\n') for line in open(os.path.join(binDir, "CLInstr_Begin2.txt"))]
if version == 1:
    lines_mid_2.append('ignore the meaning of the word and still to categorize the gender of the face image.)
else:
    lines_mid_2.append('still categorize the face image.')

lines_mid_2.append("Please memorize the task rule and press the space bar to begin.")


# Practice Instr
lines_practice = [line.rstrip('\n') for line in open(os.path.join(binDir, "CLInstr_Practice.txt"))]
lines_practice.append

# Post Forced Choice Instr
lines_post = [line.rstrip('\n') for line in open(os.path.join(binDir, "CLInstr_PostFC.txt"))]
lines_post.append

Instr_1 = visual.TextStim(win=win, name='Instr_1 ', color='black', font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None,
    text=(' '.join(map(str, lines_begin_1))))
Instr_2 = visual.TextStim(win=win, name='Instr_2 ', color='black', font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None,
    text=(' '.join(map(str, lines_begin_2))))
Instr_3 = visual.TextStim(win=win, name='Instr_3 ', color='black', font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None,
    text=(' '.join(map(str, lines_mid1))))
Instr_4 = visual.TextStim(win=win, name='Instr_4 ', color='black', font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None,
    text=(' '.join(map(str, lines_mid2))))
Instr_Practice = visual.TextStim(win=win, name='Instr_Practice', color='black', font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None,
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
        Instr_1.setAutoDraw(False)
        Instr_2.setAutoDraw(True)
    if event.getKeys(keyList=["escape"]):
        core.quit()
    win.flip()
Instr_2.setAutoDraw(False)
##---------------------------START Practice_1-------------------------------## 
theseKeys = []
trialcounter = 0
for ptrial in range(12):
    t = 0
    Practice_1_Clock.reset()
    continueRoutine = True

    ##------------------SET DURATION & ITI OF STIMULI-------------------##
    #duration 1000 ms
    duration = expmatrix.loc[ptrial,'Duration']
    
    #ITI jittering 800-2000 ms
    ITI = expmatrix.loc[ptrial,'ITI']

    ##---------------------SET STIMULI & RESPONSE---------------------------##
    stim_image = expmatrix.loc[ptrial,'stim_image']
    Image.setImage(stim_image)
    frequency = expmatrix.loc[ptrial,'Frequency']
    corrAns = expmatrix.loc[ptrial,'corrAns']
    congruency = expmatrix.loc[ptrial,'Congruency']

    if congruency != 'None':
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

    ##--------------------------WHILE LOOP BEGINS-------------------------##
    while continueRoutine:
        if event.getKeys(keyList=["escape"]):
            core.quit()
        # get current time
        t = Practice_1_Clock.getTime()
        key_resp = event.BuilderKeyResponse()

        if t < ITI:
             Blank.setAutoDraw(True)
        elif t > ITI and t < ITI + duration:
             Blank.setAutoDraw(False)
             Image.setAutoDraw(True)
             if congruency != 'None':
                 stroop_text.setAutoDraw(True)
             else:
                 pass

        else:
             Image.setAutoDraw(False)
             Blank.setAutoDraw(False)
             if congruency != 'None':
                 stroop_text.setAutoDraw(False)
             else:
                 pass
             continueRoutine = False

        theseKeys = event.getKeys(keyList=['w', 'o'])
        if len(theseKeys) > 0 and t < ITI + duration and t > duration:# at least one key was pressed
#            if theseKeys[-1] == None:
#                 key_resp.corr = 0
#                 Incorrect.setAutoDraw(True)
            #theseKeys = theseKeys[0]
            #print(theseKeys[0])
            # was this 'correct'?
            if str(corrAns) in theseKeys:
                 key_resp.corr = 1
                 Correct.setAutoDraw(True)
            else:
                 key_resp.corr = 0
                 Incorrect.setAutoDraw(True)

        ##------------CHECK ALL IF COMPONENTS HAVE FINISHED---------------##
        if continueRoutine:
             win.flip()
        else:
             Correct.setAutoDraw(False)
             Incorrect.setAutoDraw(False)
             break

##--------------------------NO NEED TO RECORD DATA-------------------------------##
    trialcounter += 1
    thisExp.nextEntry()
# completed 12 repeats of 'Practice_1'


##------------------------------START Task_1----------------------------------##
theseKeys = []
trialcounter = 0
Instr_Practice.setAutoDraw(True)
advance = 0
while advance < 1:
    if event.getKeys(keyList=["space"]):
        advance += 1
        Instr_Practice.setAutoDraw(False)
    if event.getKeys(keyList=["escape"]):
        core.quit()
    win.flip()

for trial in range(12,252):
    t = 0
    Task_1_Clock.reset()  # clock
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
    
    if congruency != 'None':
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

    ##--------------------------WHILE LOOP BEGINS-------------------------##
    while continueRoutine:
        if event.getKeys(keyList=["escape"]):
            core.quit()
        # get current time
        t = Task_1_Clock.getTime()
        key_resp = event.BuilderKeyResponse()

        ##--------------------STIMULI PRESENTATION-------------------------------##
        if t < ITI:
             Blank.setAutoDraw(True)
        elif t > ITI and t < ITI + duration:
             Blank.setAutoDraw(False)
             Image.setAutoDraw(True)
             if congruency != 'None':
                 stroop_text.setAutoDraw(True)
             else:
                 pass

        else:
             Image.setAutoDraw(False)
             Blank.setAutoDraw(False)
             if congruency != 'None':
                 stroop_text.setAutoDraw(False)
             else:
                 pass
             continueRoutine = False


        theseKeys = event.getKeys(keyList=['w', 'o'])       
        if len(theseKeys) > 0 and t < ITI + duration:# at least one key was pressed
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
# completed 240 repeats of 'Task_1'


##---------------------------START Practice_2-------------------------------## 
Instr_3.setAutoDraw(True)
advance = 0
while advance < 2:
    if event.getKeys(keyList=["space"]):
        advance += 1
        Instr_3.setAutoDraw(False)
        Instr_4.setAutoDraw(True)
    if event.getKeys(keyList=["escape"]):
        core.quit()
    win.flip()
Instr_4.setAutoDraw(False)

theseKeys = []
trialcounter = 0

for ptrial in range(252,264):
    t = 0
    Practice_2_Clock.reset()
    continueRoutine = True

    ##------------------SET DURATION & ITI OF STIMULI-------------------##
    #duration 1000 ms
    duration = expmatrix.loc[ptrial,'Duration']
    
    #ITI jittering 800-2000 ms
    ITI = expmatrix.loc[ptrial,'ITI']

    ##---------------------SET STIMULI & RESPONSE---------------------------##
    stim_image = expmatrix.loc[ptrial,'stim_image']
    Image.setImage(stim_image)
    frequency = expmatrix.loc[ptrial,'Frequency']
    corrAns = expmatrix.loc[ptrial,'corrAns']
    congruency = expmatrix.loc[ptrial,'Congruency']

    if congruency != 'None':
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

    ##--------------------------WHILE LOOP BEGINS-------------------------##
    while continueRoutine:
        if event.getKeys(keyList=["escape"]):
            core.quit()
        # get current time
        t = Practice_2_Clock.getTime()
        key_resp = event.BuilderKeyResponse()

        if t < ITI:
             Blank.setAutoDraw(True)
        elif t > ITI and t < ITI + duration:
             Blank.setAutoDraw(False)
             Image.setAutoDraw(True)
             if congruency != 'None':
                 stroop_text.setAutoDraw(True)
             else:
                 pass

        else:
             Image.setAutoDraw(False)
             Blank.setAutoDraw(False)
             if congruency != 'None':
                 stroop_text.setAutoDraw(False)
             else:
                 pass
             continueRoutine = False

        theseKeys = event.getKeys(keyList=['w', 'o'])       
        if len(theseKeys) > 0 and t < ITI + duration:# at least one key was pressed
            # was this 'correct'?
            if str(corrAns) in theseKeys:
                 key_resp.corr = 1
                 Correct.setAutoDraw(True)
            else:
                 key_resp.corr = 0
                 Incorrect.setAutoDraw(True)


        ##------------CHECK ALL IF COMPONENTS HAVE FINISHED---------------##
    
        if continueRoutine:
             win.flip()
        else:
             Correct.setAutoDraw(False)
             Incorrect.setAutoDraw(False)
             break

##--------------------------NO NEED TO RECORD DATA-------------------------------##
    trialcounter += 1
    thisExp.nextEntry()
# completed 12 repeats of 'Practice_2'

##------------------------------START Task_2----------------------------------##
theseKeys = []
trialcounter = 0
Instr_Practice.setAutoDraw(True)
advance = 0
while advance < 1:
    if event.getKeys(keyList=["space"]):
        advance += 1
        Instr_Practice.setAutoDraw(False)
    if event.getKeys(keyList=["escape"]):
        core.quit()
    win.flip()

for trial in range(264,504):
    t = 0
    overalltime = globalClock.getTime()
    Task_2_Clock.reset()  # clock
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
    
    if congruency != 'None':
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

    ##--------------------------WHILE LOOP BEGINS-------------------------##
    while continueRoutine:
        if event.getKeys(keyList=["escape"]):
            core.quit()
        # get current time
        t = Task_2_Clock.getTime()
        key_resp = event.BuilderKeyResponse()

        ##--------------------STIMULI PRESENTATION-------------------------------##
        if t < ITI:
             Blank.setAutoDraw(True)
        elif t > ITI and t < ITI + duration:
             Blank.setAutoDraw(False)
             Image.setAutoDraw(True)
             if congruency != 'None':
                 stroop_text.setAutoDraw(True)
             else:
                 pass

        else:
             Image.setAutoDraw(False)
             Blank.setAutoDraw(False)
             if congruency != 'None':
                 stroop_text.setAutoDraw(False)
             else:
                 pass
             continueRoutine = False


        theseKeys = event.getKeys(keyList=['w', 'o'])       
        if len(theseKeys) > 0 and t < ITI + duration:# at least one key was pressed
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
# completed 240 repeats of 'Task_2'


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()