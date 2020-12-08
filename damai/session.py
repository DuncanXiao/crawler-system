import requests
from selenium import webdriver

def login(ip):
  # damaiWeb = 'https://www.damai.cn/'
  # damaiWeb = 'https://www.baidu.com/'
  ipWeb = 'http://httpbin.org/ip'
  proxy = 'http://139.224.37.83:3128'
  proxies = {
    "http": proxy,
    "https": proxy
  }
  headers = {'X-Forwarded-For':'8.8.8.8'}
  # res = requests.get(ipWeb, proxies=proxies)
  res = requests.get('http://119.23.201.215/', proxies=proxies, headers=headers)
  print('yes')
  # user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36"
  # chromeOptions = webdriver.ChromeOptions()
  # chromeOptions.add_argument('--proxy-server={proxy}')
  # chromeOptions.add_argument('--user-agent=%s' % user_agent)
  # driver = webdriver.Chrome(chrome_options=chromeOptions)
  # driver.get('https://www.baidu.com/')
