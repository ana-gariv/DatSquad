import re
import requests
import urllib.request
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import sys 

BASE_URL = 'https://www.inei.gob.pe/'
#all 'a' html tags -> list
def get_all_hrefs(url):
    response = requests.get(url)

    print("OK", response)

    soup = BeautifulSoup(response.text, "html.parser")

    all_links = soup.findAll('a')

    print(f"Found {len(all_links)}")
    return all_links

#parsing obtained links and looking only for .xlsx files -> list and output .txt file
def parse_links(all_links):
    line_count = 1
    excels = []
    for link in all_links:
        if re.search("^.*[.]xlsx$", link['href']):
            excels.append(link['href'])
    with open ("xlsx_links.txt", "w") as f_ptr:
        for link in excels:
            f_ptr.write(f"{urljoin(BASE_URL, link)}\n")
        f_ptr.close()
    return excels

def main(url):
    all_links = get_all_hrefs(url)
    excels = parse_links(all_links)
    for i in excels:
        print(i)

if __name__ == "__main__":
    try:
        url = str(sys.argv[1])
        main(url)
    except:
        print("Invalid args.")
   
