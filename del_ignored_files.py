# coding: utf-8
#NAME:  del_ignored_files.py
#DESCRIPTION: This python script will delete all folders/files in the gitignore. Used to clear out files for testing main.py.

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
    MOD:     Creation of file and base functionality
    AUTHOR:  Ian Chavez
    COMMENT:
        - title
====================== END OF MODIFICATION HISTORY ============================
"""
import os
import shutil

def delete_ignored_files():
    # Get current directory
    current_directory = os.getcwd()

    # Read .gitignore file
    gitignore_path = os.path.join(current_directory, '.gitignore')
    with open(gitignore_path, 'r') as gitignore_file:
        ignored_patterns = gitignore_file.read().splitlines()

    for pattern in ignored_patterns:
        pattern_path = os.path.join(current_directory, pattern)
        
        # Check if path is directory or file, does corresponding action to del 
        if os.path.isdir(pattern_path):
            shutil.rmtree(pattern_path)
        elif os.path.isfile(pattern_path):
            os.remove(pattern_path)

if __name__ == "__main__":
    delete_ignored_files()
