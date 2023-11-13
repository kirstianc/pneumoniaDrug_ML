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
# Imports

if __name__ == '__main__':
    
    print("===== Starting pneuomoniaDrug_ML =====")
    
    print("Running GoogleSheet_scraper.py...")
    exec(open('GoogleSheet_scraper.py').read())
    print("Running chemspider_scraper.py...")
    exec(open('chemspider_scraper.py').read())
    
    print("===== Done =====")