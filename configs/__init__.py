DATA_FOLDER = "data"
DATA_CONFIGS_FILE = "data"
DATA_CONFIGS_FILE_PATH = f"{DATA_FOLDER}/{DATA_CONFIGS_FILE}"
import os
if os.path.isdir(DATA_FOLDER) == False:
    os.mkdir(DATA_FOLDER)