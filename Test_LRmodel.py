# coding: utf-8
# NAME:  Test_LRmodel.py
# DESCRIPTION: This python script will test two logistic regression models utilizing the training data and testing data found in 'datasets/'.

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
12/01/23:
    MOD:     Initial creation of file and base functionality
    AUTHOR: Shivam Amin
    COMMENT:
        - Load vectorizer and old model
        - Test old model on testing dataset
        - Load vecotrizer and new model
        - Test new model on training dataset
        - Test new model on testing dataset

12/05/23:
    MOD:     Design changes
    AUTHOR: Shivam Amin
    COMMENT:
        - Make a generic function that will load in the wanted vectorizer and model for a given dataset
        - Call this function 3 times for the tests listed in the modification history above.
====================== END OF MODIFICATION HISTORY ============================
"""
import os
import pandas as pd
import pickle
from sklearn.metrics import confusion_matrix, accuracy_score, precision_recall_fscore_support

print('---- Starting Testing_LRmodel.py ----')
# Import datasets
print('Importing datasets...')
testing_dataset = pd.read_csv('datasets/testing_dataset.csv')
training_dataset = pd.read_csv('datasets/training_dataset.csv')
validation_dataset = pd.read_csv('datasets/validation_dataset.csv')
def test_model(dataset, model_path, performance_file, model, set_name,vectorizer_name):

    # Split into X and y for testing set
    print(f'Splitting into X and y for {set_name} set...')
    smiles_data = dataset.iloc[:, :-1].values.ravel().astype(str)

    # Load the vectorizer used during testing
    print('Loading vectorizer...')
    vectorizer = pickle.load(open(f'models/{vectorizer_name}.pkl', 'rb'))

    X_test = vectorizer.transform(smiles_data)
    y_test = dataset.iloc[:, -1].values

    # Load the LR model
    print(f'Loading {model} model from {model_path}...')
    classifier = pickle.load(open(f'models/{model_path}.pkl', 'rb'))

    # Test the LR model on the testing set
    print(f'Testing {model} model on {set_name} set...')
    y_pred_test = classifier.predict(X_test)

    # Save performance for the LR model
    print(f'Saving performance for {model} model...')
    if not os.path.exists('performance'):
        os.makedirs('performance')

    with open(f'performance/{performance_file}', 'w') as f:
        f.write('Confusion Matrix:\n')
        f.write(str(confusion_matrix(y_test, y_pred_test)) + '\n')
        f.write('Accuracy:\n')
        f.write(str(accuracy_score(y_test, y_pred_test)) + '\n')
        f.write('Precision, Recall, F1:\n')
        f.write(str(precision_recall_fscore_support(y_test, y_pred_test, average='binary')) + '\n')


test_model(testing_dataset,'LRmodel','original_model_testing_performance.txt','Original LR','Testing','vectorizer')
test_model(training_dataset,'Tuned_LRmodel','tuned_model_training_performance.txt','Tuned LR','Training','vectorizer_combined')
test_model(testing_dataset,'Tuned_LRmodel','tuned_model_testing_performance.txt','Tuned LR','Testing','vectorizer_combined')