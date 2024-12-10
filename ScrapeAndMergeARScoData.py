import os
import sys

import requests as req
from loguru import logger
from selectolax.parser import HTMLParser

# Configure Loguru logger
formatColor = "<yellow>{time:YYYY-MM-DD HH:mm:ss}</yellow> | <level>{level:<8}</level> | <green><bold>{message}</bold></green>"

logger.remove()

logger.add('ARSco.log',
           rotation="500kb",
           format=formatColor,
           level="WARNING")

logger.add(sys.stderr,
           format=formatColor,
           level="INFO")


def append_data_to_file(session, links, filename):
    """Appends data from the given links to the specified file using a Session."""
    total_links = len(links)
    if total_links == 0:
        logger.warning(f"No links to process for {filename}.")
        return
    
    with open(filename, 'a') as file:
        for idx, link in enumerate(links, start=1):
            logger.info(f"Fetching data from: '{link}' ===> '{filename}'\n")
            
            try:
                response = session.get(link)
                response.raise_for_status()
                file.write(response.text + '\n')
            except req.exceptions.RequestException as e:
                logger.error(f"Failed to fetch data from: {link} - {e}")
                continue

            # Calculate percentage and display progress
            percentage = (idx / total_links) * 100
            print(f"Progress: {percentage:.2f}% ({idx}/{total_links})", end='\r')

    print(f"\nData appended to {filename} successfully.\n")


def create_data_folder():
    """Creates a folder named 'Data' if it doesn't already exist."""
    folder_name = "ARScoData"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        logger.info(f"Created folder: {folder_name}\n")
    else:
        logger.info(f"Folder already exists: {folder_name}\n")
    return folder_name


def main():
    BASE_URL = "https://www.saao.ac.za/~sbp/ARSco_Pol/"
    
    # Create the Data folder
    data_folder = create_data_folder()
    
    # Create a requests session
    with req.Session() as session:
        try:
            response = session.get(BASE_URL)
            response.raise_for_status()
        except req.exceptions.RequestException as e:
            logger.error(f"HTTP request error on {BASE_URL}: {e}")
            return

        html = HTMLParser(response.text)
        links = html.css('table tr td a')

        polar_links = []
        photo_links = []

        for link in links:
            try:
                href = link.attributes['href']
                if 'stksBMJD_S_O_B_phase' in href:
                    polar_links.append(BASE_URL + href)
                    logger.info(f"Added link: '{href}' to polar_links\n")

                elif 'photJD_BMJD_SOB' in href:
                    photo_links.append(BASE_URL + href)
                    logger.info(f"Added link: '{href}' to photo_links\n")

            except KeyError:
                logger.error(f"Missing 'href' attribute in link: {link}")

        # File paths in the ARScoData folder
        polar_file = os.path.join(data_folder, 'polarimetry.dat')
        photo_file = os.path.join(data_folder, 'photometry.dat')

        append_data_to_file(session, polar_links, polar_file)
        append_data_to_file(session, photo_links, photo_file)

        print("Data successfully saved to 'polarimetry.dat' and 'photometry.dat' in the 'ARScoData' folder.")


if __name__ == "__main__":
    main()