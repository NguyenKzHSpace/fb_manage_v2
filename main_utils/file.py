from main_utils.hash import hash,unhash
from configs import DATA_CONFIGS_FILE_PATH
import os
import json
def save_data_configs(data:dict):
    """Save dat

    Args:
        data (dict): _description_
    """
    data = hash(str(data).replace("'",'"'))
    with open(DATA_CONFIGS_FILE_PATH,"w") as file:
        file.write(data)

def read_data_configs()->(dict):
    """Read data config

    Args:
        data (dict): data
    """
    if os.path.isfile(DATA_CONFIGS_FILE_PATH) == False:
        return {}
    with open(DATA_CONFIGS_FILE_PATH,"r") as file:
        data = file.read()
    data = unhash(data)
    try:
        data = json.loads(data)
    except Exception as ex:
        return {}
    return data

def put_data_configs(key:str,data:str):
    configs_data = read_data_configs()
    configs_data[key] = data
    save_data_configs(configs_data)