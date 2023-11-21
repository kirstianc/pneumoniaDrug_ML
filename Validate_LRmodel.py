# coding: utf-8
#NAME:  Validate_LRmodel.py
#DESCRIPTION: This Python script is designed to validate the performance of a logistic regression model using the validation dataset. 
# The validation data is sourced from 'datasets/validation_dataset.csv'

"""
AUTHOR: Ian Chavez

   Unpublished-rights reserved under the copyright laws of the United States.

   This data and information is proprietary to, and a valuable trade secret
   of, Leonard P. Wesley and Ian Chavez. It is given in confidence by Leonard
   P. Wesley and Ian Chavez. Its use, duplication, or disclosure is subject to
   the restrictions set forth in the License Agreement under which it has been
   distributed.

      Unpublished Copyright © 2023 Leonard P. Wesley and Ian Chavez
      All Rights Reserved

========================== MODIFICATION HISTORY ==============================
11/21/23:
    MOD:     Initial creation of file and base functionality
    AUTHOR: Ian Chavez
    COMMENT:
        - Edit to utilize CSV instead of text files
        - Changed file save to improve directory structure
            - Creates datasets folder if it doesn't exist
====================== END OF MODIFICATION HISTORY ============================
"""
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
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(smiles_data)
y_train = validation_dataset.iloc[:, -1].values

print('Loading model...')
classifier = pickle.load(open('models/LRmodel.pkl', 'rb'))

# Validate model
print('Validating model...')
y_pred = classifier.predict(X_train)

# Save performance
print('Saving performance...')
if not os.path.exists('performance'):
    os.makedirs('performance')
with open('performance/validation_performance.txt', 'w') as f:
    f.write('Confusion Matrix:\n')
    f.write(str(confusion_matrix(y_train, y_pred)) + '\n')
    f.write('Accuracy:\n')
    f.write(str(accuracy_score(y_train, y_pred)) + '\n')
    f.write('Precision, Recall, F1:\n')
    f.write(str(precision_recall_fscore_support(y_train, y_pred, average='binary')) + '\n')
    
print('---- Finished with Validate_LRmodel.py ----')
