# coding: utf-8
# NAME:  Tune_LRmodel.py
# DESCRIPTION: This python script will tune the model from before based on the results of the validation set.

"""
AUTHOR: Shivam Amin

   Unpublished-rights reserved under the copyright laws of the United States.

   This data and information is proprietary to, and a valuable trade secret
   of, Leonard P. Wesley and Ian Chavez. It is given in confidence by Leonard
   P. Wesley and Ian Chavez. Its use, duplication, or disclosure is subject to
   the restrictions set forth in the License Agreement under which it has been
   distributed.

      Unpublished Copyright © 2023 Leonard P. Wesley and Shivam Amin
      All Rights Reserved

========================== MODIFICATION HISTORY ==============================
12/05/23:
    MOD:     Initial creation of file and base functionality
    AUTHOR: Shivam Amin
    COMMENT:
        - Create a new vectorizer
        - Make the dataset a combined set of training and validation
        - Define Grid Search
        - Test Tuned model
====================== END OF MODIFICATION HISTORY ============================
"""
import os
import pandas as pd
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, precision_recall_fscore_support
from sklearn.model_selection import train_test_split

# Import datasets
print('Importing datasets...')
training_dataset = pd.read_csv('datasets/training_dataset.csv')
validation_dataset = pd.read_csv('datasets/validation_dataset.csv')

# Combine training and validation datasets for hyperparameter tuning
combined_dataset = pd.concat([training_dataset, validation_dataset], ignore_index=True)

# Split into X and y
print('Splitting into X and y...')
smiles_data = combined_dataset['SMILES'].values.ravel().astype(str)
X_combined = smiles_data  # Keep SMILES data for vectorizer optimization
y_combined = combined_dataset['CLASS'].values

# Split combined dataset into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_combined, y_combined, test_size=0.2, random_state=42)

# Define vectorizer with default parameters (to be optimized)
vectorizer = CountVectorizer()

# Transform entire combined dataset with the vectorizer
print('Fitting and transforming vectorizer on the entire combined dataset...')
X_combined_vectorized = vectorizer.fit_transform(X_combined)

# Define logistic regression model
lr = LogisticRegression(random_state=0, max_iter=1000, solver='liblinear', penalty='l2')

# Define hyperparameter grid
param_grid = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100],
    'penalty': ['l1', 'l2']
}

# Create GridSearchCV
grid_search = GridSearchCV(lr, param_grid, cv=5, scoring='accuracy', n_jobs=-1)

# Perform hyperparameter tuning
print('Performing hyperparameter tuning...')
grid_search.fit(X_combined_vectorized, y_combined)

# Get the best hyperparameters
best_params = grid_search.best_params_
print(f'Best Hyperparameters: {best_params}')

# Refit vectorizer with optimized parameters on the entire combined dataset
print('Refitting vectorizer with optimized parameters on the entire combined dataset...')
vectorizer = CountVectorizer(**vectorizer.get_params())  # Recreate vectorizer with the same parameters
X_combined_vectorized = vectorizer.fit_transform(X_combined)

# Save the tuned model
print('Saving tuned model and vectorizer...')
if not os.path.exists('models'):
    os.makedirs('models')
pickle.dump(grid_search.best_estimator_, open('models/Tuned_LRmodel.pkl', 'wb'))
pickle.dump(vectorizer, open('models/vectorizer_combined.pkl', 'wb'))

# Test the tuned model on the validation set
X_val_vectorized = vectorizer.transform(X_val)
y_pred_val_tuned = grid_search.best_estimator_.predict(X_val_vectorized)
# Save performance for the LR model
print(f'Saving performance for Tuned LR model...')
if not os.path.exists('performance'):
    os.makedirs('performance')

with open(f'performance/tuned_model_validation_performance.txt', 'w') as f:
    f.write('Confusion Matrix:\n')
    f.write(str(confusion_matrix(y_val, y_pred_val_tuned)) + '\n')
    f.write('Accuracy:\n')
    f.write(str(accuracy_score(y_val, y_pred_val_tuned)) + '\n')
    f.write('Precision, Recall, F1:\n')
    f.write(str(precision_recall_fscore_support(y_val, y_pred_val_tuned, average='binary')) + '\n')

print('---- Finished with Tune_LRmodel.py ----')
