import requests
from bs4 import BeautifulSoup
import os
import shutil
from tkinter import filedialog
import tkinter as tk

# Function to download an image
def download_image(url, filepath):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(filepath, 'wb') as file:
            shutil.copyfileobj(response.raw, file)
    else:
        print(f"Failed to download image from {url}")

# Function to scrape images and download them
def scrape_and_download_images(url, folder_path):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        image_containers = soup.select('#graphic-game-item-listing .col-sm-6.col-md-4.col-lg-3 .card.mb-4')

        # Total number of images
        total_images = len(image_containers)
        print(f"Found {total_images} images to download.")

        downloaded_count = 0

        for index, container in enumerate(image_containers):
            img_element = container.select_one('.text-center img.submission-preview')
            player_id_element = container.select_one('.px-3 .copies-text.clickable')
            player_id = player_id_element['data-clipboard-text'] if player_id_element else None  #
            image_url = img_element['src'] if img_element else None  

            if player_id and image_url:
                image_name = f"{player_id}.png"  
                filepath = os.path.join(folder_path, image_name)
                download_image(image_url, filepath)
                downloaded_count += 1
                print(f"Downloaded {downloaded_count}/{total_images} images.")

        print("Images downloaded successfully!")
    except Exception as e:
        print(f"Error scraping images: {e}")


def select_folder_and_scrape():
    root = tk.Tk()
    root.withdraw()  
    folder_path = filedialog.askdirectory()  

    if folder_path:
        while True:
            url = input('Enter the URL (or type "exit" to quit): ')
            if url.lower() == "exit":
                print("Exiting the program.")
                break
            scrape_and_download_images(url, folder_path)
    else:
        print('No folder selected!')

# Run the scraper
if __name__ == "__main__":
    select_folder_and_scrape()
