import os
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()

source_path = os.getenv('SOURCE_PATH')
dest_path = os.getenv('DEST_PATH')

# get list of all files
arrFile = os.listdir(source_path)
#print(arrFile)
for i in arrFile:
    if (Path(i).suffix == ('.mp3')) or (Path(i).suffix == ('.wav')): # get desired file extensions
        print(i)