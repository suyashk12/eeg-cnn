import matplotlib.pyplot as plt
import numpy as np

file = np.loadtxt('SMNI_CMI_TRAIN/co2c0000342/co2c0000342.rd.029.txt', delimiter = ',')
file2 = np.loadtxt('SMNI_CMI_TRAIN/co2c0000342/co2c0000342.rd.031.txt', delimiter = ',')

fig, ax = plt.subplots(2, 1, sharex = True)
im = ax[0].imshow(file, vmin = -30, vmax = 30)
ax[0].set_ylabel('Electrode Number', fontsize = 25)
ax[0].set_title('Trial 29', fontsize = 20)
ax[1].imshow(file2, vmin = -30, vmax = 30)
ax[1].set_xlabel('Time Stamp [1/256 s]', fontsize = 25)
ax[1].set_ylabel('Electrode Number', fontsize = 25)
ax[1].set_title('Trial 31', fontsize = 20)
ax[0].tick_params(axis='y', labelsize=20)
ax[1].tick_params(axis='both', labelsize=20)
fig.suptitle('Patient 342 (Control), Stimulus = S2 nomatch', fontsize = 25)
cbar = fig.colorbar(im, ax = ax.ravel().tolist())
cbar.ax.set_ylabel('Voltage (mV)', rotation = 270, fontsize = 25)
cbar.ax.tick_params(axis='y', labelsize=20)


file3 = np.loadtxt('SMNI_CMI_TRAIN/co2a0000369/co2a0000369.rd.013.txt', delimiter = ',')
fig2, ax2 = plt.subplots()
im2 = ax2.imshow(file3, vmin = -30, vmax = 30)
ax2.set_ylabel('Electrode Number', fontsize = 25)
ax2.set_title('Patient 369 (Alcholic), Stimulus = S2 nomatch, Trial 13', fontsize = 25)
ax2.set_xlabel('Time Stamp [1/256 s]', fontsize = 25)
ax2.tick_params(axis = 'both', labelsize = 20)
cbar2 = fig.colorbar(im2, ax = ax2)
cbar2.ax.set_ylabel('Voltage (mV)', rotation  = 270, fontsize = 25)
cbar2.ax.tick_params(axis = 'y', labelsize = 20)