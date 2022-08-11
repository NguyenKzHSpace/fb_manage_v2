import requests
from .file import get_data_configs, put_data_configs, read_data_configs

def login(server:str = None, username:str = None,password:str = None):
    if server:
        put_data_configs(key = "server",data = server)
    if username:
        put_data_configs(key = "username",data = username)
    if password:
        put_data_configs(key = "password",data = password)
        
    server_url = get_data_configs(key = "server")
    url = f"{server_url}/login"
    data = {
        "email": get_data_configs(key = "email"),
        "password": get_data_configs(key = "password")
    }
    res = requests.post(url=url, json=data,timeout=5)
    ##
    # Response error
    # #
    if res.status_code != 200:
        return False
    try:
        res = res.json()
        s_key = res.get("secret_key")
        token = res.get("token").get("token_type")+" " + \
            res.get("token").get("access_token")
        code = res.get("code")
        put_data_configs(key = "s_key",data = s_key)
        put_data_configs(key = "token",data = token)
        put_data_configs(key = "code",data = code)
        print(f"Token: {token} ")
        return True
    except Exception as ex:
        return False
    return False
    
def call_api(method:str,api:str,data:dict = {},timeout:int = 20):
    data_configs = read_data_configs()
    header = {
        "Authorization": data_configs.get('token'),
        "s-key": data_configs.get('s_key')
    }
    url = f"{data_configs.get('server')}/{api}"
    res = None
    if method=="post":
        res = requests.post(url, json=data, headers=header, timeout=timeout)
    elif method == "get":
        res = requests.get(url, json=data, headers=header, timeout=timeout)
    elif method == "put":
        res = requests.put(url, json=data, headers=header, timeout=timeout)
    if res.status_code == 401:
        if login() == False:
            return None
    else:
        return res
    
    data_configs = read_data_configs()
    header = {
        "Authorization": data_configs.get('token'),
        "s-key": data_configs.get('s_key')
    }
    url = f"{data_configs.get('server')}/{api}"
    res = requests.post(url, json=data, headers=header, timeout=timeout)
    return res
        