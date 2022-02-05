import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.svm import SVC
import pickle

import sys

# Create and save a machine learning model to predict gender based on audio data
def main(audio_path):
    # Read the csv audio data
    data = pd.read_csv(audio_path)

    # Drop all the features we were unable to calculate
    train = data.drop(columns=['sp.ent', 'sfm', 'centroid', 'meanfun', 'minfun', 'maxfun', 'meandom', 'mindom', 'maxdom', 'dfrange', 'modindx'])

    # Split data into training and testing datasets
    X = train.drop(columns=['label'])
    y = train['label']
    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # Create and train model
    model = SVC(kernel='linear', C=2.0, probability=True)

    model.fit(X_train, y_train)

    # Test and print accuracy of model
    y_pred = model.predict(X_test)
    score = model.score(X_test, y_test)
    print(score)

    from sklearn import metrics

    # Model Accuracy: how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    
    
    # Save model to disk
    filename = 'trained_svc_model.sav'
    pickle.dump(model, open(filename, 'wb'))



if __name__=='__main__':
    audio_path = 'sample_audio/voice.csv'
    main(audio_path)

