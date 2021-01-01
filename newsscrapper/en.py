import requests
import re

def CNNSC():
  CNN=requests.get("http://rss.cnn.com/rss/edition")
  arcnn=re.findall(r'<item>(.*?)</item>',CNN.text)
  data={}
  for i in range(len(arcnn)):
    picture=re.findall(r'<media:content medium="image" url="(.*?)"',arcnn[i])
    link=re.findall(r'<link>(.*?)</link>',arcnn[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0]}
    except:
      data[str(i)]={"link":link[0],"img":""}

  return data



def FoxNewsSC():
  FoxNews=requests.get("http://feeds.foxnews.com/foxnews/latest")
  s=FoxNews.text
  s=s.replace("\n","")
  arfoxnews=re.findall(r'<item>(.*?)</item>',s)
  data={}
  for i in range(len(arfoxnews)):
    picture=re.findall(r'<media:content url="(.*?)"',arfoxnews[i])
    link=re.findall(r'<link>(.*?)</link>',arfoxnews[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0]}
    except:
      data[str(i)]={"link":link[0],"img":""}

  return data


def ABCNewsSC():
  ABCNews=requests.get("https://abcnews.go.com/abcnews/moneyheadlines")
  s=ABCNews.text
  s=s.replace("\n","")
  arabcnews=re.findall(r'<item>(.*?)</item>',s)
  data={}
  for i in range(len(arabcnews)):
    picture=re.findall(r'<media:thumbnail url="(.*?)"',arabcnews[i])
    link=re.findall(r'<link><!\[CDATA\[(.*?)]]>',arabcnews[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0]}
    except:
      data[str(i)]={"link":link[0],"img":""}

  return data



def TheGuardianSC():
  TheGuardianSC=requests.get("https://www.theguardian.com/us-news/rss")
  s=TheGuardianSC.text
  s=s.replace("\n","")
  arguardian=re.findall(r'<item>(.*?)</item>',s)
  data={}
  for i in range(len(arguardian)):
    picture=re.findall(r'url="https://i.guim.co.uk/img/media/(.*?)"',arguardian[i])
    link=re.findall(r'<link>(.*?)</link>',arguardian[i])
    try:
      data[str(i)]={"link":link[0],"img":"https://i.guim.co.uk/img/media/"+picture[0].replace("amp;","")}
    except:
      data[str(i)]={"link":link[0],"img":""}

  return data

