import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.svm import SVC
import pickle


# Create and save machine learning model to predict presence of Parkinson's
def main(data_path):
    # Read in audio data of Parkinson's patients
    data = pd.read_csv(data_path)

    # Split data into training and testing subsets
    X = data.drop(columns=['status', 'name'])
    y = data['status']

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    # Create model
    model = SVC(kernel='linear', C=2.0, probability=True)
    model.fit(X_train, y_train)
    
    # Get and print accuracy score of model
    y_pred = model.predict(X_test)
    score = model.score(X_test, y_test)
    print(score)

    # Save machine learning model to disk
    filename = 'trained_parkinsons_model.sav'
    pickle.dump(model, open(filename, 'wb'))


if __name__ == '__main__':
    data_path = 'sample_audio/parkinsons_data.csv'
    main(data_path)
