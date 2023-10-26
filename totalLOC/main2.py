import os

arr = []
mypath = r"E:\Projects\kafka"

with open('../data/loc.txt', 'w') as file:
    for dirpath, dirnames, filenames in os.walk(mypath):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            lines = 0
            try:
                with open(full_path, 'r', errors="ignore") as file1:
                    lines = len(file1.readlines())
            except Exception as e:
                print(f"Error reading {full_path}: {str(e)}")
            file.write(f"{full_path}~{lines}\n")
