import os
import openai
from dotenv import load_dotenv
import csv


with open('data1_val_23cent.csv', 'r', encoding='utf-8') as f_in, open('output.csv', 'w', newline='', encoding='utf-8') as f_out:
    rdr = csv.reader(f_in)
    writer = csv.writer(f_out)
    for line in rdr:
        writer.writerow([line[3], line[4]])