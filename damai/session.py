import requests

def login(ip):
  damaiWeb = 'https://www.damai.cn/'
  proxies = {
   'http': ip,
   'https': ip
  }
  data = requests.get(damaiWeb)
  print(data)