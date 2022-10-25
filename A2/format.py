import pandas as pd
import os

def format(entries):
    for entry in entries:
        if (entry.endswith('docx')): 
            print("SKIPPED:   " + entry)
            continue

        df = pd.read_csv('raw_data/' + entry, skiprows=1, usecols=[0,3,4,5],header=None)
        df.to_csv('formatted_data/' + entry, encoding='utf-8', index=False, header=False)
        print("FORMATTED: " + entry)


def main():
    entries = os.listdir('raw_data/')
    format(entries)

if __name__ == "__main__":
    main()
