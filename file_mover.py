import os
import sys
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
# GLOBAL VARIABLES
source_path = os.getenv('SOURCE_PATH')
dest_path = os.getenv('DEST_PATH')
intType = "a"
numSources = 2
flgFinalSourcePath = False
flgFinalDestPath = False
arrFileTypes = [['.png','.jpeg','.jpg','.bmp'],['.mp3','.wav','.flac','.ogg'],['.mp4','.mov','.aiv','.flv']]

## Quit program if no files in location
def file_list_check(array_of_files):
    if (len(array_of_files) <= 0):
        print("No files in source location to check. Program ending.")
        sys.exit(0)

## Move files based on extension
def file_move(intFileType, source, destination):
    arrFile = os.listdir(source_path)
    file_list_check(arrFile)
    for i in arrFile:
        for j in arrFileTypes[intFileType]: # loop through arrFileTypes
            if (Path(i).suffix == (j)):
                src_path = os.path.join(source, i)
                dst_path = os.path.join(destination, i)
                os.rename(src_path, dst_path)
                print(i + ' has been moved')
                break
    print("All files moved. Program ending.")
    sys.exit(0)

def build_target_path(source, flagTrigger):
    tempDirList = [name for name in os.listdir(source)
            if os.path.isdir(os.path.join(source, name))] # get current dirs in dir
    # loop and print them all
    max_choices = 0
    for i in enumerate(tempDirList):
        print(str(i[0] + 1) + ". " + str(i[1]))
        max_choices = i[0] + 1
    # append a "finished path" option that makes finalSourceDir = true
    print("**" + str(max_choices+1) + ". FINALISE DESTINATION**")
    int_add = "a"
    while int_add.isnumeric() == False or int(int_add) <=0 or int(int_add) > int(max_choices + 1):
        int_add = input("Enter Number: ")
    if int(int_add) == int(max_choices + 1):
        flagTrigger = True
        return source, flagTrigger
    else:
        source = source + "\\" + str(tempDirList[int(int_add)-1]) # MINUS 1 FOR 0 BASED COUNTING
        return source, flagTrigger

if __name__ == "__main__":
    # path check
    print("Welcome!")

    ## BUILD SOURCE ##
    print("First we will build your source path")
    # loop until source directory granted
    while flgFinalSourcePath == False:
        source_path, flgFinalSourcePath = build_target_path(source_path, flgFinalSourcePath)
    print("Your final source path is " + str(source_path))

    ## BUILD DESTINATION ##
    print("Secondly we will build your destination path")
    while flgFinalDestPath == False:
        dest_path, flgFinalDestPath = build_target_path(dest_path, flgFinalDestPath)
    print("Your final destination path is " + str(dest_path))

    ## GET FILE TYPE ##
    while intType.isnumeric() == False or int(intType) <= 0 or int(intType) > 3:
        # get file type to move
        print("Please choose your desired type of file to move.")
        print("1. Common image types")
        print("2. Common audio types")
        print("3. Common video types")
        intType = input("Enter Number: ")
    intType = int(intType)
    intType -= 1 #-1 to match arrFileTypes array

    ## MOVE FILES ##
    file_move(intType, source_path, dest_path)
