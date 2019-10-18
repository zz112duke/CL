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
Practice_1_Clock = core.Clock() #unlike globalclock, gets reset each trial
Practice_2_Clock = core.Clock()
Task_1_Clock = core.Clock()
Task_2_Clock = core.Clock()

##########Version##########
# version 1 [non,con] version 2 [con,non]
version = random.choice([1,2])
#print (version)


##########Stimuli##########
Imagelist1 = list(os.listdir(_thisDir + '/Set1'))
Imagelist1 = ["Set1/" + i for i in Imagelist1]

Imagelist2 = list(os.listdir(_thisDir + '/Set2'))
Imagelist2 = ["Set2/" + i for i in Imagelist2]

Practicelist = list(os.listdir(_thisDir + '/Practice'))
Practicelist = ["Practice/" + i for i in Practicelist]
#print(Practicelist)

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

Instr_Post = visual.TextStim(win=win, name='blank', text='Now you will be presented with images that you have seen in the main experiment. Indicate which one was presented in the main experiment more frequently by clicking on the image. Press the space bar to contiune. ', 
    font=u'Arial', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'black', colorSpace='rgb', opacity=1, depth=0.0)


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
stim_image1 = Practicelist*3 + stim_image_high1 +stim_image_medium1 + stim_image_low1

random.shuffle(Imagelist2)
stim_image_high2 = [Imagelist2[i] for i in indices_high]*10
stim_image_medium2 = [Imagelist2[i] for i in indices_medium]*5
stim_image_low2 = [Imagelist2[i] for i in indices_low]
stim_image2 = Practicelist*3 + stim_image_high2 +stim_image_medium2 + stim_image_low2
#print (stim_image2)
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
frequency = ['N/A']*12 + ['high']*80 + ['medium']*80 + ['low']*80
#frequency_practice = ['N/A']*12

##########Congruency##########
congruency_con = ['con']*6 + ['incon']*6 + ['con']*40 + ['incon']*40 + ['con']*40 + ['incon']*40 + ['con']*40 + ['incon']*40
#congruency_con_practice = ['con']*6 + ['incon']*6
congruency_non = ['N/A']*252


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
expmatrix_non_exp = expmatrix_non[12:252].sample(frac=1).reset_index(drop=True)
expmatrix_non_prac = expmatrix_non[0:12].sample(frac=1).reset_index(drop=True)

expmatrix_con = [image_set[1], frequency, congruency_con, corrAns2, duration, ITI]
expmatrix_con = pd.DataFrame(expmatrix_con)
expmatrix_con = expmatrix_con.transpose()
expmatrix_con.columns = ['stim_image','Frequency','Congruency','corrAns','Duration','ITI']
expmatrix_con_exp = expmatrix_con[12:252].sample(frac=1).reset_index(drop=True)
expmatrix_con_prac = expmatrix_non[0:12].sample(frac=1).reset_index(drop=True)


if version == 1:
    expmatrix = pd.concat([expmatrix_non_prac , expmatrix_non_exp, expmatrix_con_prac, expmatrix_con_exp],ignore_index=True)
else:
    expmatrix = pd.concat([expmatrix_con_prac, expmatrix_con_exp, expmatrix_non_prac , expmatrix_non_exp],ignore_index=True)


##--------------Post Forced Choice Matrix---------------##
# Generate a matrix with F1 vs. F2, where F1 column has 40 'Low' and F2 has 20 'Medium' and 20 'High'. 
# F1_path & F2_path: 20 Low from Set1 and 20 from Set2; 10 medium from Set1 and 10 from Set2; 10 High from Set1 and 10 from Set2
# Task_1 & Task_2, where each has 20 columns saying 'con' & 'non'
# Question: 20 says 'higher' and 20 says 'lower'.
# Correct response

F1 = ['Low'] *40
F2 = ['Medium'] * 20 + ['High'] * 20
Question = ['higher'] * 20 + ['lower'] * 20

F1_path = expmatrix.loc[(expmatrix.Congruency == 'N/A') & (expmatrix.Frequency == 'Low')]
print (F1_path)










