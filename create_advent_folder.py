#!/usr/bin/env python3
import os
import argparse

def create_advent_folder(day_number):
    folder_name = str(day_number)
    
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
        print(f"Folder '{folder_name}' created.")
    else:
        print(f"Folder '{folder_name}' already exists.")
    
    files_to_create = ["data.txt", f"{folder_name}a.py", f"{folder_name}b.py"]
    
    for file_name in files_to_create:
        file_path = os.path.join(folder_name, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                # Optionally, add boilerplate code for Python files
                if file_name.endswith(".py"):
                    f.write(f"# Solution for Day {day_number}, Part {file_name[len(folder_name):len(folder_name)+1].upper()}\n\n")
                print(f"File '{file_name}' created in '{folder_name}'.")
        else:
            print(f"File '{file_name}' already exists in '{folder_name}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Advent of Code folder structure.")
    parser.add_argument("day", type=int, help="Day number for the Advent of Code")
    args = parser.parse_args()

    create_advent_folder(args.day)
