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


Post_Instr_1 = visual.TextStim(win=win, name='Post_Instr_1', color='black',
    text='Welcome to the post-test! You will answer a few questions about the experimental stimuli and do some judgement tasks. Press the spacebar to continue.')

Post_Q1 = visual.TextStim(win=win, name='Post_Q1', color='black',
    text='Did you notice that the presentation frequency of the images varied? Press Y if you noticed and N if you did not.')
    
Post_Q2 = visual.TextStim(win=win, name='Post_Q2', color='black',
    text='In this session, you will see some images from the main experiment that you just finished. If you know or can guess the presentation frequencies of these images, press the corresponding key (e.g., if you think it was presented very frequently, press 3; moderately frequently, press 2; not frequently press 1). If you do not know and cannot guess, then press enter. There is no time limit to respond if you are uncertain about your response. Press the spacebar to begin.')

###PostImage###
os.chdir(_thisDir + '/Stimuli_faces1')
Imagelist = list(os.listdir())
os.chdir(_thisDir)


posttrials = 30
ITI_min = 800.0
ITI_max = 2000.0

postImage = 

postmatrix = [postImage, [random.randint(fix_duration_min, fix_duration_max) for i in range(posttrials)]]