import os
from glob import glob

for root, dirs, files in os.walk("playground"):
    print(f"root: {root}, dirs: {dirs}, files: {files}")
    for each_file in files:
        print(os.path.join(root, each_file))
