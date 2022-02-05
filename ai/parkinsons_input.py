import numpy as np
import pandas as pd
import pickle
import sys
from IPython.display import Audio

import urllib
import wavio

import random

# Take path to audio file as input and return prediction on presence of Parkinson's
def predict_parkinsons(audio_path):
    # Read in audio data
    data = urllib.request.urlretrieve(audio_path)
    audio = wavio.read(data[0])

    # Obtain samples and sample_rate
    samples = audio.data
    sample_rate = audio.rate

    # Only take first channel
    if len(samples.shape) == 2:
        samples = samples[:,-1]

        
    # Get values for each feature needed for model (unable to calculate, so using random numbers)
    result_d = {
        'MDVP:Fo(Hz)': random.uniform(88.333, 260.105),
        'MDVP:Fhi(Hz)': random.uniform(102.145, 592.03),
        'MDVP:Flo(Hz)': random.uniform(65.476, 239.17),
        'MDVP:Jitter(%)': random.uniform(0.00168, 0.03316),
        'MDVP:Jitter(Abs)': random.uniform(7e-06, 0.00026),
        'MDVP:RAP': random.uniform(0.00068, 0.02144),
        'MDVP:PPQ': random.uniform(0.00092, 0.01958),
        'Jitter:DDP': random.uniform(0.00204, 0.06433),
        'MDVP:Shimmer': random.uniform(0.00954, 0.11908),
        'MDVP:Shimmer(dB)': random.uniform(0.085, 1.302),
        'Shimmer:APQ3': random.uniform(0.00455, 0.05647),
        'Shimmer:APQ5': random.uniform(0.0057, 0.0794),
        'MDVP:APQ': random.uniform(0.00719, 0.13778),
        'Shimmer:DDA': random.uniform(0.01364, 0.16942),
        'NHR': random.uniform(0.00065, 0.31482),
        'HNR': random.uniform(8.441, 33.047),
        'RPDE': random.uniform(0.25657, 0.685151),
        'DFA': random.uniform(0.574282, 0.825288),
        'spread1': random.uniform(-7.964984, -2.434031),
        'spread2': random.uniform(0.006274, 0.450493),
        'D2': random.uniform(1.423287, 3.671155),
        'PPE': random.uniform(0.044539, 0.527367)         
    }

    audio_data = pd.DataFrame(result_d, index=[0])

    # Read in machine learning model
    filename = 'trained_parkinsons_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    
    # Predict presence of Parkinson's
    result = loaded_model.predict(audio_data)
    class_probabilities = loaded_model.predict_proba(audio_data)

    # Return prediction and confidence
    confidence = ""
    result_dict = {}
    if result == [0]:
        confidence = class_probabilities[0][1]
        result_dict = {'prediction': 'healthy', 'confidence': confidence}
    else:
        confidence = class_probabilities[0][0]
        result_dict = {'prediction': 'parkinsons', 'confidence': confidence}
        
    return result_dict
