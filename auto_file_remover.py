import os
from dotenv import load_dotenv
load_dotenv()

source_path = os.getenv('SOURCE_PATH')
print(source_path)
isExist = os.path.exists(source_path)
print(isExist)