from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def init_Chrome_Driver(proxy_user_name:str,proxy_password:str,proxy_ip:str,proxy_port:str) -> (webdriver.Chrome):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
   
    chrome_options.add_argument(
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39')


    wire_options = {}
    wire_options['proxy'] = {
        'https': f'https://{proxy_user_name}:{proxy_password}@{proxy_ip}:{proxy_port}'}

    driver = webdriver.Chrome(ChromeDriverManager().install(),
                              options=chrome_options,
                              seleniumwire_options=wire_options)
    driver.set_window_size(1366, 600)
    return driver

