import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, accuracy_score, precision_recall_fscore_support

print('---- Starting Validate_LRmodel.py ----')
# Import datasets
print('Importing datasets...')
validation_dataset = pd.read_csv('datasets/validation_dataset.csv')

# Split into X and y
print('Splitting into X and y...')
smiles_data = validation_dataset.iloc[:, :-1].values.ravel().astype(str)  # Convert numpy array to list of strings

# Load the vectorizer and transform the data
print('Loading vectorizer...')
vectorizer = pickle.load(open('models/vectorizer.pkl', 'rb'))
X_val = vectorizer.transform(smiles_data)
y_val = validation_dataset.iloc[:, -1].values

print('Loading model...')
classifier = pickle.load(open('models/LRmodel.pkl', 'rb'))

# Validate model
print('Validating model...')
y_pred = classifier.predict(X_val)

# Save performance
print('Saving performance...')
if not os.path.exists('performance'):
    os.makedirs('performance')
with open('performance/validation_performance.txt', 'w') as f:
    f.write('Confusion Matrix:\n')
    f.write(str(confusion_matrix(y_val, y_pred)) + '\n')
    f.write('Accuracy:\n')
    f.write(str(accuracy_score(y_val, y_pred)) + '\n')
    f.write('Precision, Recall, F1:\n')
    f.write(str(precision_recall_fscore_support(y_val, y_pred, average='binary')) + '\n')
    
print('---- Finished with Validate_LRmodel.py ----')