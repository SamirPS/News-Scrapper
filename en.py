import requests
import re

def CNNSC():
  CNN=requests.get("http://rss.cnn.com/rss/edition")
  arcnn=re.findall(r'<link>(.*?)</link>',CNN.text)
  del arcnn[0]
  return arcnn

def FoxNewsSC():
  FoxNews=requests.get("http://feeds.foxnews.com/foxnews/latest")
  arfoxnews=re.findall(r'<link>(.*?)</link>',FoxNews.text)
  del arfoxnews[0]
  del arfoxnews[0]
  return arfoxnews
