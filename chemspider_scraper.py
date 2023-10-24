# coding: utf-8
#NAME:  chemspider_scraper.py
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
====================== END OF MODIFICATION HISTORY ============================
"""
# Imports
import requests
from bs4 import BeautifulSoup
import time

# Links to scrape, obtained from chemspiderLinks.txt
list_of_cslinks = []

def obtain_chemspider_links():
    with open('chemspiderLinks.txt', 'r') as f:
        for line in f:
            list_of_cslinks.append(line.strip())


def scrape_chemspider_links():
    for link in list_of_cslinks:
        response = requests.get(link, verify=False)

        # If success
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the SMILE string
            smile_string = soup.find('span', id='ctl00_ctl00_ContentSection_ContentPlaceHolder1_RecordViewDetails_rptDetailsView_ctl00_moreDetails_WrapControl2')

            # If the SMILE string exists, write it to a file --> separated by <wbr> & spaces, fixed by replacing spaces w empty string
            if smile_string:
                smiles_text = smile_string.get_text(separator=" ").replace(" ", "")
                with open('chemspider_smileStrings.txt', 'a') as f:
                    f.write(smiles_text + '\n')
            else:
                print("Could not find SMILE string.")
                break # Break out because SMILE string not found --> prevents future error
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

        # Sleep for 1 second to prevent overloading the server
        time.sleep(1)

if __name__ == '__main__':
    print("Obtaining ChemSpider links...")
    obtain_chemspider_links()
    print("Scraping ChemSpider links...")
    scrape_chemspider_links()
    print("Done.")