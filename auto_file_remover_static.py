import os
import sys

from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

source_path = os.getenv('SOURCE_PATH')
dest_path = os.getenv('DEST_PATH')

# get list of all files
arrFile = os.listdir(source_path)
#print(arrFile)
if (len(arrFile) <= 0):
    print("No files in source location. Program ending.")
    sys.exit(0)

for i in arrFile:
    if (Path(i).suffix == ('.mp3')) or (Path(i).suffix == ('.wav')): # get desired file extensions
        src_path = os.path.join(source_path, i)
        dst_path = os.path.join(dest_path, i)
        os.rename(src_path, dst_path)
        print(i + ' has been moved')
    print("All files moved. Program ending.")
    sys.exit(0)