# coding: utf-8
#NAME:  Train_LRmodel.py
#DESCRIPTION: This python script will train a logistic regression model utilizing the training data found in 'datasets/training_dataset.csv'.

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
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer

# Import datasets
print('Importing datasets...')
training_dataset = pd.read_csv('datasets/training_dataset.csv')

# Split into X and y
print('Splitting into X and y...')
smiles_data = training_dataset.iloc[:, :-1].values.ravel().astype(str)  # Convert numpy array to list of strings
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(smiles_data)
y_train = training_dataset.iloc[:, -1].values

# Train model
print('Training model...')
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Save model
print('Saving model...')
if not os.path.exists('models'):
    os.makedirs('models')
pickle.dump(classifier, open('models/LRmodel.pkl','wb'))

# Save performance
from sklearn.metrics import confusion_matrix, accuracy_score, precision_recall_fscore_support
y_pred = classifier.predict(X_train)
cm = confusion_matrix(y_train, y_pred)

if not os.path.exists('performance'):
    os.makedirs('performance')
with open('performance/LRmodel_performance.txt', 'w') as f:
    f.write('Confusion Matrix:\n')
    f.write(str(cm))
    f.write('\nAccuracy Score: ')
    f.write(str(accuracy_score(y_train, y_pred)))
    f.write('\n')
    f.write('Precision, Recall, F1 Score:\n')
    f.write(str(precision_recall_fscore_support(y_train, y_pred, average='weighted')))



