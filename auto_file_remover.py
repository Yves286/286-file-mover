import os

path_to_scan = "" # folder that program will check
# check location exists
isExist = os.path.exists(path_to_scan)
print(isExist)