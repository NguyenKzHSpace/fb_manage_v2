from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
def init_Chrome_Driver(proxy_user_name:str,proxy_password:str,proxy_ip:str,proxy_port:str) -> (tuple[webdriver.Chrome,str]):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--disable-logging')  
 
    wire_options = {}
    wire_options['proxy'] = {
        'https': f'https://{proxy_user_name}:{proxy_password}@{proxy_ip}:{proxy_port}',
        'http': f'http://{proxy_user_name}:{proxy_password}@{proxy_ip}:{proxy_port}'}

    
    driver = webdriver.Chrome(ChromeDriverManager().install(),
                              options=chrome_options,
                              seleniumwire_options=wire_options)
    
    
    try:
        driver.get("https://ifconfig.me/")
        if driver.find_elements(By.ID,"ip_address")[0].text != proxy_ip:
            return None,"Proxy connection lost."
    except Exception as ex:
        return None,"Proxy connection lost."

    return driver, "Ok"

