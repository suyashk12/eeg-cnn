import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


stimulus = 'S2 nomatch,'

x = np.arange(0, 256)

cdict = {}
adict = {}

for i in x:
    
    cdict[i] = []
    adict[i] = []
    
summary = pd.read_csv('SMNI_CMI_TRAIN/patient_summary.csv')

patients = []
[patients.append(x) for x in summary['Patient'] if x not in patients]

for patient in patients:
    
    trials = np.array(summary.loc[(summary['Stimulus'] == stimulus) & (summary['Patient'] == patient), 'Trial'])
    
    for trial in trials:
        
        file = np.loadtxt('SMNI_CMI_TRAIN/' + patient + '/' + patient + '.rd.' + '0'*(3-len(str(trial))) + str(trial) + '.txt', delimiter = ',')
        
        for i in range(0, 64):
            
            for j in x:
                
                if patient[3] == 'c':
                    
                    cdict[j].append(file[i][j])
                    
                elif patient[3] == 'a':
                    
                    adict[j].append(file[i][j])
                    
cmeans = []
ameans = []
cstds = []
astds = []

for i in x:
    
    cmeans.append(np.mean(cdict[i]))
    ameans.append(np.mean(adict[i]))
    cstds.append(np.std(cdict[i]) / np.sqrt(len(cdict[i])))
    astds.append(np.std(adict[i]) / np.sqrt(len(adict[i])))
    
cmeans = np.array(cmeans)
ameans = np.array(ameans)
cstds = np.array(cstds)
astds = np.array(astds)
    
fig, ax = plt.subplots()
ax.fill_between(x, cmeans + cstds, cmeans - cstds, color = 'darkblue', zorder = 1, alpha = 0.3)
ax.fill_between(x, ameans + astds, ameans - astds, color = 'darkred', zorder = 1, alpha = 0.3)
ax.plot(x, cmeans, c = 'darkblue', zorder = 5, label = 'Control Patients')
ax.plot(x, ameans, c = 'darkred', zorder = 5, label = 'Alcoholic Patients')
ax.set_title('Averaged Voltage vs Time, all electrodes, all patients, stimulus = S2 nomatch', fontsize = 25)
ax.set_xlabel('Time Stamp [1/256 s]', fontsize = 25)
ax.set_ylabel('Voltage [mV]', fontsize = 25)
ax.legend(loc = 'lower left', fontsize = 25)
ax.tick_params(axis = 'both', labelsize = 20)