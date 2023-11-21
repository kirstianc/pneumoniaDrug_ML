# coding: utf-8
#NAME:  GoogleSheet_scraper.py
#DESCRIPTION: This python script will scrape ChemSpider links from Google Sheets.

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
11/13/23:
    MOD:     Creation of file and base functionality
    AUTHOR:  Ian Chavez
    COMMENT:
        - Runs Python files in order
====================== END OF MODIFICATION HISTORY ============================
"""
if __name__ == '__main__':
    
    print("===== Starting pneuomoniaDrug_ML =====")
    exec(open('scrapers/GoogleSheet_scraper.py').read())
    exec(open('scrapers/Chemspider_scraper.py').read())
    exec(open('Dataset_editor.py').read())
    # Train model using training dataset
    # Validate model using validation dataset
    # Test model using testing dataset
    # Save model and performance to text file for later use
    print("===== Done =====")