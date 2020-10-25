import requests
import random

def iPVerify(ip):
  # http://xckfeimao.top/
  targetUrl = 'http://httpbin.org/ip'
  proxies = {
   'http': ip,
   'https': ip
  }
  tunnel = random.randint(1,10000)
  headers = {"Proxy-Tunnel": str(tunnel)}
  try:
    requests.get(targetUrl, proxies=proxies, headers=headers)
  except requests.exceptions.RequestException as e:
    print('proxy error: ---', e)
  else:
    return True


if __name__ == "__main__":
  print('hahha')