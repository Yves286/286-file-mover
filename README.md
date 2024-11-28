# auto_file_remover

> python script moves file based on attributes

A flexible script that runs in the background, reads incoming files and automatically moves them to a new location.

2 versions have been been planned for this project:

### Static Version

Provided in file ```auto_file_remover_static.py``` is a one-time program that reads the current files in the directory and move them to the destination. When done it will immediately terminate.

## .env File Sample

SOURCE_PATH is the directory that the program is scanning.
DEST_PATH is the target directory that files will be moved to.

```
SOURCE_PATH = 'C:\Users\{User}\Downloads'
DEST_PATH = 'C:\Users\{User}\Music\unsorted_audio'
```
