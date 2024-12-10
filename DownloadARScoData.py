import os
import requests
from selectolax.parser import HTMLParser
from loguru import logger

logger.add("ARScoData.log", 
           format="{time} {level} {message}", 
           level="INFO", 
           rotation="500KB")

BASE_URL, DATA_DIR = "https://www.saao.ac.za/~sbp/ARSco_Pol/", "ARScoData"
os.makedirs(DATA_DIR, exist_ok=True)

def fetch_page_content(session, url):
    try:
        response = session.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        logger.error(f"Error fetching {url}: {e}")
        return None

def scrape_files(session, base_url, patterns):
    content = fetch_page_content(session, base_url)
    if content:
        parser = HTMLParser(content)
        for link in parser.css("table tr td a"):
            href = link.attributes.get("href", "")
            if any(pattern in href for pattern in patterns):
                save_file(session, base_url + href, href)

def save_file(session, file_url, filename):
    filepath = os.path.join(DATA_DIR, filename)
    if os.path.exists(filepath): return
    try:
        response = session.get(file_url, stream=True)
        response.raise_for_status()
        with open(filepath, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
        logger.info(f"File saved: {filename}")
    except requests.RequestException as e:
        logger.error(f"Error downloading {file_url}: {e}")

def main():
    with requests.Session() as session:
        scrape_files(session, BASE_URL, ["stksBMJD_S_O_B_phase", "photJD_BMJD_SOB"])

if __name__ == "__main__":
    main()