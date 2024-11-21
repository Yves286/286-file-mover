import os
import sys
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
# GLOBAL VARIABLES
source_path = os.getenv('SOURCE_PATH')
dest_path = os.getenv('DEST_PATH')
intType = "a"
arrFileTypes = [['.png','.jpeg','.jpg','.bmp'],['.mp3','.wav','.flac','.ogg'],['.mp4','.mov','.aiv','.flv']]

# get list of all files
arrFile = os.listdir(source_path)

def file_list_check(): # quit program if no files in location
    if (len(arrFile) <= 0):
        print("No files in source location. Program ending.")
        sys.exit(0)

def file_move(intFileType): # moves files based on extension
    for i in arrFile:
        for j in arrFileTypes[intFileType]: # loop through arrFileTypes
            if (Path(i).suffix == (j)):
                src_path = os.path.join(source_path, i)
                dst_path = os.path.join(dest_path, i)
                os.rename(src_path, dst_path)
                print(i + ' has been moved')
                break
    print("All files moved. Program ending.")
    sys.exit(0)

if __name__ == "__main__":
    while intType.isnumeric() == False:
        print("Please choose your desired type of file to move.")
        print("1. Common image types")
        print("2. Common audio types")
        print("3. Common video types")
        intType = input("Enter Number: ")
    intType = int(intType)
    intType -= 1 #-1 to match arrFileTypes array
    file_move(intType)
