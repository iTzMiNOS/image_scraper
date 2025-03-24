import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import base64
import time

def create_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def scroll_down(driver, scroll_pause_time=2, scroll_limit=5):
    last_height = driver.execute_script("return document.body.scrollHeight")
    for i in range(scroll_limit):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scrape_all_images(driver):
    try:
        images = driver.find_elements(By.TAG_NAME, 'img')
        image_urls = []
        for img in images:
            image_url = img.get_attribute('src') or img.get_attribute('data-src')
            if image_url and "data:image/gif" not in image_url:
                width = int(img.get_attribute('width') or 0)
                height = int(img.get_attribute('height') or 0)
                if width >= 100 and height >= 100:
                    image_urls.append(image_url)
        return image_urls
    except Exception as e:
        print(f"Error scraping images: {e}")
        return []

def save_image(image_url, folder_name, file_name, retry_count=3):
    try:
        file_path =os.path.join(folder_name, f"{file_name}.jpg")

        if image_url.startswith('data:image/'):
            header, encoded = image_url.split(',', 1)
            image_data = base64.b64decode(encoded)
            with open(file_path, 'wb') as f:
                f.write(image_data)

        else:
            for attempt in range(retry_count):
                response = requests.get(image_url, timeout=10)
                if response.status_code == 200:
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    break
                else:
                    print(f"Failed attempt {attempt+1} for image: {image_url}")
                    time.sleep(2)
    except Exception as e:
        print(f"Error saving image {file_name}: {e}")

def scrape_and_save_images(base_folder, search_term, num_images=10):
    driver = create_driver()
    folder_path = os.path.join(base_folder, f"{'_'.join(search_term.split())}")

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    driver.get(f"https://www.google.com/search?q={search_term}&tbm=isch")
    time.sleep(5)
    scroll_down(driver)
    image_urls = scrape_all_images(driver)
    image_urls = image_urls[:num_images]
    for index, image_url in enumerate(image_urls, start=1):
        file_name = f'{search_term}_{index}'
        save_image(image_url, folder_path, file_name)
    print(f"Finished scraping")
    driver.quit()

if __name__ == "__main__":
    base_folder = r"C:\Users\Amir\Desktop\endangered_species"
    endangered_species = [
    "Amur Leopard",
    "Javan Rhino",
    "Sumatran Tiger",
    "Mountain Gorilla",
    "Vaquita",
    "Yangtze Giant Softshell Turtle",
    "Saola",
    "Axolotl",
    "Orangutan (Bornean and Sumatran)",
    "Amur Tiger",
    "Kakapo",
    "Black Rhino",
    "Sunda Pangolin",
    "Indian Elephant",
    "Pygmy Three-Toed Sloth",
    "Siberian Crane",
    "California Condor",
    "White Rhino (Southern)",
    "Hawksbill Turtle",
    "Red Panda",
    "Asian Elephant",
    "Giant Panda",
    "Snow Leopard",
    "West Indian Manatee",
    "Numbat",
    "Bengal Tiger",
    "Addax Antelope",
    "Spix’s Macaw",
    "Golden Poison Dart Frog",
    "Saiga Antelope",
    "Lemur (Various species)",
    "African Wild Dog",
    "Chilean Flamingo",
    "Mexican Gray Wolf",
    "Yellow-eyed Penguin",
    "Great White Shark",
    "Sunda Clouded Leopard"
]
    endangered_species_with_severity = [
    {"species": "Amur Leopard", "status": "Critically Endangered (CR)"},
    {"species": "Javan Rhino", "status": "Critically Endangered (CR)"},
    {"species": "Sumatran Tiger", "status": "Critically Endangered (CR)"},
    {"species": "Mountain Gorilla", "status": "Endangered (EN)"},
    {"species": "Vaquita", "status": "Critically Endangered (CR)"},
    {"species": "Yangtze Giant Softshell Turtle", "status": "Critically Endangered (CR)"},
    {"species": "Saola", "status": "Critically Endangered (CR)"},
    {"species": "Axolotl", "status": "Critically Endangered (CR)"},
    {"species": "Orangutan (Bornean and Sumatran)", "status": "Critically Endangered (CR)"},
    {"species": "Amur Tiger", "status": "Endangered (EN)"},
    {"species": "Kakapo", "status": "Critically Endangered (CR)"},
    {"species": "Black Rhino", "status": "Critically Endangered (CR)"},
    {"species": "Sunda Pangolin", "status": "Critically Endangered (CR)"},
    {"species": "Indian Elephant", "status": "Endangered (EN)"},
    {"species": "Pygmy Three-Toed Sloth", "status": "Critically Endangered (CR)"},
    {"species": "Siberian Crane", "status": "Critically Endangered (CR)"},
    {"species": "California Condor", "status": "Critically Endangered (CR)"},
    {"species": "White Rhino (Southern)", "status": "Near Threatened (NT)"},
    {"species": "Hawksbill Turtle", "status": "Critically Endangered (CR)"},
    {"species": "Red Panda", "status": "Endangered (EN)"},
    {"species": "Asian Elephant", "status": "Endangered (EN)"},
    {"species": "Giant Panda", "status": "Vulnerable (VU)"},
    {"species": "Snow Leopard", "status": "Vulnerable (VU)"},
    {"species": "West Indian Manatee", "status": "Endangered (EN)"},
    {"species": "Numbat", "status": "Endangered (EN)"},
    {"species": "Bengal Tiger", "status": "Endangered (EN)"},
    {"species": "Addax Antelope", "status": "Critically Endangered (CR)"},
    {"species": "Spix's Macaw", "status": "Extinct in the Wild (EW)"},
    {"species": "Golden Poison Dart Frog", "status": "Endangered (EN)"},
    {"species": "Saiga Antelope", "status": "Critically Endangered (CR)"},
    {"species": "Lemur (Various species)", "status": "Endangered (EN)"},
    {"species": "African Wild Dog", "status": "Endangered (EN)"},
    {"species": "Chilean Flamingo", "status": "Near Threatened (NT)"},
    {"species": "Mexican Gray Wolf", "status": "Critically Endangered (CR)"},
    {"species": "Yellow-eyed Penguin", "status": "Endangered (EN)"},
    {"species": "Great White Shark", "status": "Vulnerable (VU)"},
    {"species": "Sunda Clouded Leopard", "status": "Vulnerable (VU)"}
]


    """search_terms = persian_foods.split('\n')
    for search_term in search_terms:
        scrape_and_save_images(base_folder, search_term, num_images=50) """
    search_terms =[
        "fesenjan",
        "ghormeh sabzi",
        "tahchin",
        "khoresht gheymeh",
        "kabab koobideh",
        "halim bademjan",
        "ash reshteh",
        "kookoo sabzi",
        "shole zard",
        "shekar polo",
        "baghali polo",
        "zereshk polo",
        "faloodeh",
        "kaleh pacheh",
        "abgoosht",
        "estamboli polo",
        "zeytoon parvardeh",
        "mast o khiar",
        "mirza ghasemi",
        "baghali ghatogh"
    ]
    for search_term in endangered_species:
        scrape_and_save_images(base_folder, search_term, num_images=100)