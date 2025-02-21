import argparse
from pathlib import Path
import pandas as pd
import re

class List_Handler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_name = re.sub('.txt', '', Path(file_path).name)
        self.lines_list = []
        self.class_list = []

    def open_read(self):
        with open(self.file_path, 'r') as f:
            self.lines_list = f.readlines()

    def get_class_names(self):
        self.class_list = [re.sub(r'_', ' ', re.sub(r'^[^.]*\.', '', line.split(' ')[-1]).strip()) for line in self.lines_list]

    def list_2_csv(self):
        df = pd.DataFrame(self.class_list, columns=["classes"])
        df.to_csv(f"{self.file_name}.csv", index = True)

    def process(self): #all functions
        self.open_read()
        self.get_class_names()
        self.list_2_csv()

def main():
    parser = argparse.ArgumentParser(description="Insert file path: \n")
    parser.add_argument("file_path", type=str, help="Path to input file")

    args = parser.parse_args()
    handler = List_Handler(args.file_path)
    handler.process()

if __name__ == "__main__":
    main()






