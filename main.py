# coding: utf-8
# NAME:  GoogleSheet_scraper.py
# DESCRIPTION: This python script will scrape ChemSpider links from Google Sheets.

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
11/28/23:
    MOD:     Add input to use either Google Sheets or txt files
    AUTHOR:  Ian Chavez
    COMMENT:
        - Title
====================== END OF MODIFICATION HISTORY ============================
"""
if __name__ == "__main__":
    print("===== Starting pneuomoniaDrug_ML =====")

    # Take input from user to use either Google Sheets or txt files
    google = input("Use Google Sheets? (y/n): ")
    if google == "y" or google == "Y" or google == "yes" or google == "Yes":
        exec(open("scrapers/GoogleSheet_scraper.py").read())
    else:
        print("Using txt files in /txt/ directory")

    # Take input from user to scrape links or not
    scrape = input("Scrape links? (y/n): ")
    if scrape == "y" or scrape == "Y" or scrape == "yes" or scrape == "Yes":
        exec(open("scrapers/Chemspider_scraper.py").read())
    else:
        print("Assuming links are already scraped in /txt/ directory")
        
    exec(open("Dataset_editor.py").read())
    exec(open("Train_LRmodel.py").read())
    exec(open("Validate_LRmodel.py").read())
    # Test model using testing dataset
    # Save model and performance to text file
    print("===== Done =====")
