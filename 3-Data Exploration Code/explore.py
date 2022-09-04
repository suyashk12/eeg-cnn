import matplotlib.pyplot as plt
import numpy as np
import os
from mpl_toolkits import mplot3d
from scipy.optimize import curve_fit as cf
import pandas as pd

stimulus = 'S2 nomatch,'
series =  np.arange(0,64)

def fit(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

x = np.arange(0, 256)

summary = pd.read_csv('SMNI_CMI_TRAIN/patient_summary.csv')

patients = []
[patients.append(x) for x in summary['Patient'] if x not in patients]

fig, ax = plt.subplots()

vals_avg_c_list = []
vals_avg_a_list = []
std_avg_c_list = []
std_avg_a_list = []

cused = False
aused = False

for patient in patients: 

    if patient[3] == 'c':
        color = 'darkblue'
        if not cused:
            lab = 'Control'
            cused = True
        else:
            lab = '_nolegend_'
    elif patient[3] == 'a':
        color = 'darkred'
        if not aused:
            lab = 'Alcoholic'
            aused = True
        else:
            lab = '_nolegend_'

    trials = np.array(summary.loc[(summary['Stimulus'] == stimulus) & (summary['Patient'] == patient), 'Trial'])
    
    vals_list = []
    std_list = []
    for trial in trials:
        
        file = np.loadtxt('SMNI_CMI_TRAIN/' + patient + '/' + patient + '.rd.' + '0'*(3-len(str(trial))) + str(trial) + '.txt', delimiter = ',')
        
        
        vals_list.append(np.mean(list(file[series]), axis = 0))
        std_list.append(np.std(list(file[series]), axis = 0))
        
    
    vals = np.mean(vals_list, axis = 0)
    std = np.mean(std_list, axis = 0)

    if patient[3] == 'c':
        vals_avg_c_list.append(vals)
        std_avg_c_list.append(std)
    elif patient[3] == 'a':
        vals_avg_a_list.append(vals)
        std_avg_a_list.append(std)

    ax.plot(x, vals, c = color, label = lab)    
    

ax.set_title('Averaged Voltage vs Time, all electrodes, stimulus = S2 nomatch', fontsize = 25)
ax.set_xlabel('Time Stamp [1/256 s]', fontsize = 25)
ax.set_ylabel('Voltage [mV]', fontsize = 25)
ax.legend(loc = 'lower left', fontsize = 25)
ax.tick_params(axis='both', labelsize=20)
      
vals_avg_c = np.mean(vals_avg_c_list, axis = 0)
vals_avg_a = np.mean(vals_avg_a_list, axis = 0)
std_avg_c = np.mean(std_avg_c_list, axis = 0) / np.sqrt(np.shape(std_avg_c_list)[0])
std_avg_a = np.mean(std_avg_a_list, axis = 0) / np.sqrt(np.shape(std_avg_c_list)[0])

fig2, ax2 = plt.subplots()
ax2.fill_between(x, vals_avg_c + std_avg_c, vals_avg_c - std_avg_c, color = 'darkblue', zorder = 1, alpha = 0.3)
ax2.fill_between(x, vals_avg_a + std_avg_a, vals_avg_a - std_avg_a, color = 'darkred', zorder = 1, alpha = 0.3)
ax2.plot(x, vals_avg_c, c = 'darkblue', zorder = 5, label = 'Control Patients')
ax2.plot(x, vals_avg_a, c = 'darkred', zorder = 5, label = 'Alcoholic Patients')
ax2.set_title('Averaged Voltage vs Time, all electrodes, all patients, stimulus = S2 nomatch', fontsize = 25)
ax2.set_xlabel('Time Stamp [1/256 s]', fontsize = 25)
ax2.set_ylabel('Voltage [mV]', fontsize = 25)
ax2.legend(loc = 'lower left', fontsize = 25)
ax2.tick_params(axis = 'both', labelsize = 20)