import proxy.verify
import damai.session

if __name__ == '__main__':
  ip = '60.217.155.211:8060'
  # res = proxy.verify.iPVerify('60.217.155.211:8060')
  # print(res)
  # if(res):
  damai.session.login(ip)