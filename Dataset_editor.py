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
====================== END OF MODIFICATION HISTORY ============================
"""

working_data = []
notworking_data = []

def obtain_data():
    # Obtain working and not working SMILES data from txt files
    with open('working_smiles.txt', 'r') as f:
        working_data = f.readlines()
    with open('notworking_smiles.txt', 'r') as f:
        notworking_data = f.readlines()
    return working_data, notworking_data

def create_datasets(working_data, notworking_data):
    # training 70%, validation 15%, testing 15%


if __name__ == '__main__':
    
    print("---- Starting Dataset_editor.py ----")

    # Obtain working and not working SMILES data from txt files
    working_data, notworking_data = obtain_data()

    print("---- Finished with Dataset_editor.py ----")