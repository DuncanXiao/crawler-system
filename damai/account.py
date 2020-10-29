import requests


# python -> 大麦网账号登陆 -> 获取所有cookie -> 尝试获取个人信息.

class Account:
  __init__(self, cookie):
    self.cookie = cookie


