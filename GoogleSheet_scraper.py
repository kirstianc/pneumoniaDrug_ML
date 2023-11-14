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
        - Pull ChemSpider links from Google sheets instead of txt file
        - Creates 2 txt files: 
            - working_links.txt = SMILE strings of working compounds
            - notworking_links.txt = SMILE strings of non-working compounds
====================== END OF MODIFICATION HISTORY ============================
"""
# Imports
import gspread

# List of links to scrape, obtained from Google Sheets
list_working = []
list_notworking = []

def access_sheet():
    gc = gspread.service_account()
    sh = gc.open("ChemSpider_links")
    
    # Working compounds
    curr_wsh = sh.get_worksheet(0)
    list_working = curr_wsh.get_all_values()

    # Not working compounds
    curr_wsh = sh.get_worksheet(1)
    list_notworking = curr_wsh.get_all_values()
    
    return list_working, list_notworking
    
def save_to_files(list_working, list_notworking):
    # Save lists to files
    with open('working_links.txt', 'w') as f:
        for item in list_working:
            f.write("%s\n" % item)
    
    with open('notworking_links.txt', 'w') as f:
        for item in list_notworking:
            f.write("%s\n" % item)

if __name__ == '__main__':
    print("---- Starting GoogleSheet_scraper.py ----")
    
    print("Accessing Google Sheets...")
    list_working, list_notworking = access_sheet()
    
    print("Saving to files...")
    save_to_files(list_working, list_notworking)
    
    print("---- Finished with GoogleSheet_scraper.py ----\n")