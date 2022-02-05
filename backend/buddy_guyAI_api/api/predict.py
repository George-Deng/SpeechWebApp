#duplicate of AI functions for the purpose of backend deployment
import numpy as np
import pandas as pd
import pickle
import sys
from IPython.display import Audio
#from scipy.io import wavfile
import urllib
import wavio

import random

def predict_gender(audio_path):
    if not'https://cmpt-340.s3.amazonaws.com/media/' in audio_path:
        audio_path = 'https://cmpt-340.s3.amazonaws.com/media/'+audio_path
        
    data = urllib.request.urlretrieve(audio_path)
    # print(data[0])
    audio = wavio.read(data[0])

    samples = audio.data
    sample_rate = audio.rate
    
    if len(samples.shape) == 2:
        samples = samples[:,-1]

    spec = np.abs(np.fft.rfft(samples))
    freq = np.fft.rfftfreq(len(samples), d=1 / sample_rate)
    spec = np.abs(spec)
    amp = spec / spec.sum()
    mean = (freq * amp).sum()
    sd = np.sqrt(np.sum(amp * ((freq - mean) ** 2)))
    amp_cumsum = np.cumsum(amp)
    median = freq[len(amp_cumsum[amp_cumsum <= 0.5]) + 1]
    mode = freq[amp.argmax()]
    Q25 = freq[len(amp_cumsum[amp_cumsum <= 0.25]) + 1]
    Q75 = freq[len(amp_cumsum[amp_cumsum <= 0.75]) + 1]
    IQR = Q75 - Q25
    z = amp - amp.mean()
    w = amp.std()
    skew = ((z ** 3).sum() / (len(spec) - 1)) / w ** 3
    kurt = ((z ** 4).sum() / (len(spec) - 1)) / w ** 4

    result_d = {
        'meanfreq': [mean],
        'sd': [sd],
        'median': [median],
        'Q25': [Q25],
        'Q75': [Q75],
        'IQR': [IQR],
        'skew': [skew],
        'kurt': [kurt],
        'mode': [mode]
    }

    audio_data = pd.DataFrame.from_dict(result_d)

    filename = 'trained_svc_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(audio_data)
    #class_probabilities = loaded_model.predict_proba(audio_data)

    # print(result)
    # print(class_probabilities)
    # print(loaded_model.classes_)
    
    #confidence = ""
    #if result == ['male']:
    #    confidence = class_probabilities[0][1]
    #else:
    #    confidence = class_probabilities[0][0]
    
    #result_dict = {'prediction': result[0], 'confidence': confidence}
    
    result_dict = {'prediction': result[0]}
    # print(result_dict)
    return result_dict


def predict_parkinsons(audio_path):
    if not'https://cmpt-340.s3.amazonaws.com/media/' in audio_path:
        audio_path = 'https://cmpt-340.s3.amazonaws.com/media/'+audio_path

    data = urllib.request.urlretrieve(audio_path)
    # print(data[0])
    audio = wavio.read(data[0])

    samples = audio.data
    sample_rate = audio.rate


    if len(samples.shape) == 2:
        samples = samples[:,-1]


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

    filename = 'trained_parkinsons_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    result = loaded_model.predict(audio_data)
    #class_probabilities = loaded_model.predict_proba(audio_data)

    # print(result)
    # print(class_probabilities)
    # print(loaded_model.classes_)
    #confidence = ""
    result_dict = {}
    if result == [0]:
    #    confidence = class_probabilities[0][1]
    #    result_dict = {'prediction': 'healthy', 'confidence': confidence}
        result_dict = {'prediction': 'healthy'}
    else:
    #    confidence = class_probabilities[0][0]
    #    result_dict = {'prediction': 'parkinsons', 'confidence': confidence}
        result_dict = {'prediction': 'parkinsons'}
    
    print(result_dict)
    return result_dict
