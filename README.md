# file_mover

> python script moves file based on attributes

A script that can be run through the terminal, reads incoming files and automatically moves them to a new location.

It can move 3 categories of files:
* Images: .png, .jpeg, .jpg, .bmp
* Audios: .mp3, .wav, .flac, .ogg
* Videos: .mp4, .mov, .avi, .flv

## Execution

Provided in file ```auto_file_remover_static.py``` is a one-time program that reads the current files in the directory and move them to the destination. The program automatically prompts and lists directories for both the source and destination to further specify their paths respectively. This program can go down, but not up the file tree. Options are listed in the terminal. Only integers need to be entered.

The code can be executed in command prompt or terminal with the standard python command:

```python file_mover.py```

## .env File

The program requires a .env file to get the initial source and destination paths.

SOURCE_PATH is the initial directory path that the program will use. It can scan and list directories within to further specify the source path.

DEST_PATH is the target directory that files will be moved to. It can scan and list directories within to further specify the destination path.

Below is an example .env file intended to move audio files. It should be in the same folder as ```file_mover.py```

```
SOURCE_PATH = 'C:\Users\{User}\Downloads'
DEST_PATH = 'C:\Users\{User}\Music\unsorted_audio'
```
