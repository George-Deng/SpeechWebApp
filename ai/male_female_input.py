import numpy as np
import pandas as pd
import aubio
import pickle
import sys
from IPython.display import Audio
import urllib
import wavio

# Take path to an audio file as input, return a prediction of gender
def predict_gender(audio_path):
    # read audio path          
    data = urllib.request.urlretrieve(audio_path)
    audio = wavio.read(data[0])
    
    # Obtain samples and sample_rate
    samples = audio.data
    sample_rate = audio.rate
    
    # Only take first channel
    if len(samples.shape) == 2:
        samples = samples[:,-1]

    # Calculate features
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

    # Put features into dictionary
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

    # Read in the machine learning model
    filename = 'trained_svc_model.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    
    # Make prediction
    result = loaded_model.predict(audio_data)
    class_probabilities = loaded_model.predict_proba(audio_data)
    
    # Return result with confidence of prediction
    confidence = ""
    if result == ['male']:
        confidence = class_probabilities[0][1]
    else:
        confidence = class_probabilities[0][0]
    
    result_dict = {'prediction': result[0], 'confidence': confidence}
    # print(result_dict)
    return result_dict

# print(predict_gender("./sample_audio/cough.wav"))


