import pandas as pd
import json

df = pd.read_csv('C:/Users/Amir/Desktop/AI Course/Google-Image-Scraper/data/metadata.csv', encoding='ISO-8859-1')

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

status_dict = {'_'.join(entry["species"].split(' ')): entry["status"] for entry in endangered_species_with_severity}

df['severity'] = df['text'].map(status_dict)

df.to_csv('updated_file.csv', index=False)

print("Updated CSV file has been saved as 'updated_file.csv'.")
