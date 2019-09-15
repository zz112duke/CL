import pandas as pd
import numpy as np
import random
import copy
import os

currentDir = os.getcwd()
outputPath = os.getcwd() + os.sep + 'ExpMatrix'

##########Version##########
# version 1 [non,con] version 2 [con,non]
version = ['1','2']
current_version = random.choice(version)

#if version =='1':
#    task = ['non','con']
#else:
#    task = ['con','non']


##########Stimuli#########

###Image Set###
os.chdir(currentDir + '/Stimuli_faces1')
Imagelist1 = list(os.listdir())
os.chdir('..')

os.chdir(currentDir + '/Stimuli_faces2')
Imagelist2 = list(os.listdir())


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


###Timing###
trials = 240
duration = 3.0
ITI_min = 800.0
ITI_max = 2000.0
stim_image = []

ITI = []
#ITI & duration
for i in range(240):
    ITI.append(random.randint(ITI_min, ITI_max)/1000)

duration = [duration]*240


###frequency###
frequency = ['high']*80 + ['medium']*80 + ['low']*80

###congruency###
congruency_con = ['con']*40 + ['incon']*40 + ['con']*40 + ['incon']*40 + ['con']*40 + ['incon']*40
congruency_non = ['N/A']*240

###corrAns###
corrAns = []
for i in stim_image:
    if ('m' or 'M') in i:
        corrAns.append('w')
    else:
        corrAns.append('o')

###Exp Matrix###
image_set = [stim_image1,stim_image2]
random.shuffle(image_set)

#Turn Exp Matrix into df to randomize rows
expmatrix_non = [image_set[0], frequency, congruency_non, corrAns, duration, ITI]
expmatrix_non = pd.DataFrame(expmatrix_non)
expmatrix_non = expmatrix_non.transpose()
expmatrix_non.columns = ['ImageSet','Frequency','Congruency','corrAns','Duration','ITI']
expmatrix_non = expmatrix_non.sample(frac=1).reset_index(drop=True)

expmatrix_con = [image_set[1], frequency, congruency_con, corrAns, duration, ITI]
expmatrix_con = pd.DataFrame(expmatrix_con)
expmatrix_con = expmatrix_con.transpose()
expmatrix_con.columns = ['ImageSet','Frequency','Congruency','corrAns','Duration','ITI']
expmatrix_con = expmatrix_con.sample(frac=1).reset_index(drop=True)
#print (expmatrix_con)
#print(len(expmatrix_con))



if version == '1':
    expmatrix = pd.concat([expmatrix_non , expmatrix_con])
else:
    expmatrix = pd.concat([expmatrix_con , expmatrix_non])

print (expmatrix)
print (len(expmatrix))













