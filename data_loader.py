from datasets import load_dataset

dataset = load_dataset("imagefolder", data_dir="C:/Users/Amir/Desktop/AI Course/Google-Image-Scraper/data", drop_labels=True)

dataset.push_to_hub("iTzMiNOS/endangered-species-with-severity")