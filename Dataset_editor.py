# coding: utf-8
#NAME:  Dataset_editor.py
#DESCRIPTION: This python script will create 3 datasets: training, validation, testing from the working and not working SMILES data.

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
11/14/23:
    MOD:     Creation of file and base functionality
    AUTHOR:  Ian Chavez
    COMMENT:
        - Obtains working and not working SMILES data from txt files, divides and shuffles into:
            - Training dataset
            - Validation dataset
            - Testing dataset
11/21/23:
    MOD:     
    AUTHOR: Ian Chavez
    COMMENT:
        - Edit to utilize CSV instead of text files
        - Changed file save to improve directory structure
            - Creates datasets folder if it doesn't exist
====================== END OF MODIFICATION HISTORY ============================
"""
import os
import pandas as pd
from sklearn.model_selection import train_test_split

working_data = []
notworking_data = []

def obtain_data():
    # Obtain working and not working SMILES data from txt files
    with open('txt/working_smiles.txt', 'r') as f:
        working_data = f.readlines()
    with open('txt/notworking_smiles.txt', 'r') as f:
        notworking_data = f.readlines()
        
    # Remove \n from strings
    working_data = [x.strip() for x in working_data]
    notworking_data = [x.strip() for x in notworking_data]
    
    return working_data, notworking_data

def create_datasets(working_data, notworking_data):
    # Create dataset folder if it doesn't exist
    if not os.path.exists('datasets'):
        os.makedirs('datasets')
    
    # Create combination dataset with corresponding amount of labels
    all_data = working_data + notworking_data
    labels = ['working'] * len(working_data) + ['not working'] * len(notworking_data)

    # Split data into training (70%), validation and testing (30% total = 15% each)
    X_train, X_temp, y_train, y_temp = train_test_split(all_data, labels, test_size=0.3, random_state=42)
    # Split data into validation (50%) and testing (50%) --> 50% of 30% = 15% 
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

    # Create DataFrames for training, validation, and testing
    train_df = pd.DataFrame({'SMILES': X_train, 'CLASS': y_train})
    val_df = pd.DataFrame({'SMILES': X_val, 'CLASS': y_val})
    test_df = pd.DataFrame({'SMILES': X_test, 'CLASS': y_test})

    # Save datasets to CSV files in datasets folder
    print("Saving training dataset to CSV file...")
    train_df.to_csv('datasets/training_dataset.csv', index=False)
    print("Saving validation dataset to CSV file...")
    val_df.to_csv('datasets/validation_dataset.csv', index=False)
    print("Saving testing dataset to CSV file...")
    test_df.to_csv('datasets/testing_dataset.csv', index=False)

    return train_df, val_df, test_df



if __name__ == '__main__':
    
    print("---- Starting Dataset_editor.py ----")

    print("Obtaining data...")
    # Obtain working and not working SMILES data from txt files
    working_data, notworking_data = obtain_data()
    
    print("Creating datasets...")
    # Create combination dataset with corresponding amount of labels
    train_df, val_df, test_df = create_datasets(working_data, notworking_data)

    print("---- Finished with Dataset_editor.py ----")