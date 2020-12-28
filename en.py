import requests
import re

def CNNSC():
  CNN=requests.get("http://rss.cnn.com/rss/edition")
  arcnn=re.findall(r'<link>(.*?)</link>',CNN.text)
  del arcnn[0]
  return arcnn
