
# 📝FM24 faces downloader tool
This project is a Python-based web scraper designed to download player images from [sortitoutsi](https://sortitoutsi.net/graphics/browse/1) using BeautifulSoup. It allows users to scrape face images and save them to a selected folder.



## Tech Stack

- Python
- requests (HTTP requests)
- BeautifulSoup (HTML parsing and web scraping)
- tkinter (for folder selection)
- shutil (for file operations)

## Prerequisites

- Python 3.x: Ensure Python is installed on your machine.
- Required Libraries: Install dependencies using pip.

## Installation



- Clone the repository:
```bash
git clone https://github.com/your-username/image-scraper.git
```

- Navigate to the project directory:
```bash
cd image-scraper
```

- Install dependencies:
```bash
pip install requests beautifulsoup4 tk
```

## Features

- **Image Scraping**: Scrapes images from a web page by selecting specific HTML elements.
- **Download Images**: Downloads images to a user-specified folder.
- **Custom Folder** Selection: Uses a dialog to allow users to choose a folder for saving images.
- **Error Handling**: Includes error handling for failed downloads or incorrect webpage structures.


## How to Use

1. Run the script:
```bash
python image_scraper.py
```
2. The program will ask you to select a folder where the images will be saved.
3. Input the URL of the webpage .
4. The script will download all available images to the selected folder.
