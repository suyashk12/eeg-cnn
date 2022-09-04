This file outlines the various steps of our analysis and mentions the relevant notebooks/ scripts used to execute the step.

DATA ACQUISITION (author: Suyash)

Step 1: Error file detection in the full data set. Contained in 1-EEG_EDA_err_detection.ipynb.
Step 2: Construction of summary CSVs and HDF5 files for later usage. Contained in 2-EEG_EDA_hdf5_full.ipynb.

DATA EXPLORATION (author: Max)

Step 3: Exploring/ averaging over various dimensions. Contained in Python scripts within the folder 3-Data Exploration Code


DATA PREPARATION (author: Zooey)

Step 4: Trying out various denoising methods. Done over notebooks 4a-simple denoising.ipynb, 4b-simple fft.ipynb, and 4c-wavelet denoising.ipynb


MODEL SELECTION AND TRAINING 

Step 5: Baseline MLP and CNN models. The MLP training is contained in 5-EEG_keras_nn_S2_nonmatch.ipynb (author: Suyash), and CNN related experiments are contained in the folder 5-CNN_Hyperparam_Tuning_Training_Set (author: Nick)

MODEL FINE-TUNING (author: Suyash)

Step 6: Hyperparameter tuning, done for each stimulus over notebooks 6a-EEG_keras_hyperparam_S1.ipynb, 6b-EEG_keras_hyperparam_S2_match.ipynb, 6c-EEG_keras_hyperparam_S2_nonmatch.ipynb
Step 7: Model training on the full data set, done over notebooks 7a-EEG_keras_cnn_S1.ipynb, 7b-EEG_keras_cnn_S2_match.ipynb, and 7c-EEG_keras_cnn_S2_nonmatch.ipynb

FINAL MODEL EVALUATION (author: Suyash)

Step 8: Computing metrics for each classifier, done over notebooks 8a-EEG_keras_evaluate_S1.ipynb, 8b-EEG_keras_evaluate_S2_match.ipynb, and 8c-EEG_keras_evaluate_S2_nonmatch.ipynb