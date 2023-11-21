# coding: utf-8
#NAME:  Chemspider_scraper.py
#DESCRIPTION: This python script will scrape SMILE strings from ChemSpider and save them to a file.

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
10/24/23:
    MOD:     Creation of file and initial organization
    AUTHOR:  Ian Chavez
    COMMENT:
        - Created file and added initial organization
        - Base functionaltiy
11/13/23:
    MOD:     Adjusting functionality
    AUTHOR:  Ian Chavez
    COMMENT:
        - Pulls from 2 txt files: 
            - working_links.txt = SMILE strings of working compounds
            - notworking_links.txt = SMILE strings of non-working compounds
11/21/23:
    MOD:    Edit to improve CSV saving + timing
    AUTHOR: Ian Chavez
    COMMENT:
        - adjusted to not have w or f
        - adjusted timing to .25 seconds from .5 seconds
====================== END OF MODIFICATION HISTORY ============================
"""
# Imports
import requests
from bs4 import BeautifulSoup
import time
import certifi

# List of links to scrape
list_working = []
list_notworking = []

def obtain_chemspider_links(file_name: str, list_of_cslinks: list):
    with open(file_name, 'r') as f:
        for line in f:
            list_of_cslinks.append(line.strip()[2:-2])
    return list_of_cslinks


def scrape_chemspider_links(working: bool, list_of_cslinks: list):

    for link in list_of_cslinks:
        cert_path = certifi.where()
        response = requests.get(link, verify=cert_path)

        # If success
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the SMILE string
            smile_string = soup.find('span', id='ctl00_ctl00_ContentSection_ContentPlaceHolder1_RecordViewDetails_rptDetailsView_ctl00_moreDetails_WrapControl2')

            # If the SMILE string exists, write it to a file --> separated by <wbr> & spaces, fixed by replacing spaces w empty string
            if smile_string:
                smiles_text = smile_string.get_text(separator=" ").replace(" ", "")
                
                if working:
                    with open('working_smiles.txt', 'a') as f:
                        f.write(smiles_text + '\n')
                else:
                    with open('notworking_smiles.txt', 'a') as f:
                        f.write(smiles_text + '\n')
                
            else:
                print("Could not find SMILE string.")
                break # Break out because SMILE string not found --> prevents future error
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

        # Sleep for .25 seconds to prevent overloading the server
        time.sleep(.25)

if __name__ == '__main__':
    print("---- Starting Chemspider_scraper.py ----")
    
    print("Obtaining Working ChemSpider links...")
    list_working = obtain_chemspider_links('working_links.txt', list_working)
    
    # Create/Clear Working file
    with open('working_smiles.txt', 'w'):
        pass
    
    print("Scraping Working SMILE data...")
    scrape_chemspider_links(True, list_working)
    
    print("Obtaining Not Working ChemSpider links...")
    list_notworking = obtain_chemspider_links('notworking_links.txt', list_notworking)
    
    # Create/Clear Not Working file
    with open('notworking_smiles.txt', 'w'):
        pass
    
    print("Scraping Not Working SMILE data...")
    scrape_chemspider_links(False, list_notworking)
    
    print("---- Finished with Chemspider_scraper.py ----\n")