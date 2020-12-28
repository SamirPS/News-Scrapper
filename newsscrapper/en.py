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

def ABCNewsSC():
  ABCNews=requests.get("https://abcnews.go.com/abcnews/moneyheadlines")
  arabcnews=re.findall(r'<link><!\[CDATA\[(.*?)]]>',ABCNews.text)
  return arabcnews

def TheGuardianSC():
  TheGuardianSC=requests.get("https://www.theguardian.com/us-news/rss")
  arguardian=re.findall(r'<link>(.*?)</link>',TheGuardianSC.text)
  del arguardian[0]
  del arguardian[0]
  return arguardian
