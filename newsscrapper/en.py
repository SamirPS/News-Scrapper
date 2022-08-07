import requests
import re

def CNNSC():
  CNN=requests.get("http://rss.cnn.com/rss/edition")
  arcnn=re.findall(r'<item>(.*?)</item>',CNN.text)
  data={}
  for i in range(len(arcnn)):
    
    picture=re.findall(r'<media:content medium="image" url="(.*?)"',arcnn[i])
    link=re.findall(r'<link>(.*?)</link>',arcnn[i])
    title=re.findall(r'<title><!\[CDATA\[(.*?)]]>',arcnn[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0],"title":title[0].replace(u"\xa0"," ")}
    except:
      data[str(i)]={"link":link[0],"img":"","title":title[0].replace(u"\xa0"," ")}

  return data


def FoxNewsSC():
  FoxNews=requests.get("http://feeds.foxnews.com/foxnews/latest")
  s=FoxNews.text
  s=s.replace("\n","")
  arfoxnews=re.findall(r'<item>(.*?)</item>',s)
  data={}
  for i in range(len(arfoxnews)):
    picture=re.findall(r'<media:content url="(.*?)"',arfoxnews[i])
    link=re.findall(r'<guid isPermaLink="true">(.*?)</guid>',arfoxnews[i])
    title=re.findall(r'<title>(.*?)</title>',arfoxnews[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0],"title":title[0].replace(u"\xa0"," ")}
    except:
      data[str(i)]={"link":link[0],"img":"","title":title[0].replace(u"\xa0"," ")}

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
    title=re.findall(r'<title><!\[CDATA\[(.*?)]]',arabcnews[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0],"title":title[0].replace(u"\xa0"," ")}
    except:
      data[str(i)]={"link":link[0],"img":"","title":title[0].replace(u"\xa0"," ")}

  return data



def TheGuardianSC():
  TheGuardianSC=requests.get("https://www.theguardian.com/us-news/rss")
  s=TheGuardianSC.text
  s=s.replace("\n","")
  arguardian=re.findall(r'<item>(.*?)</item>',s)
  data={}
  for i in range(len(arguardian)):
    picture=re.findall(r'<media:content width="140" url="(.*?)"',arguardian[i])
    link=re.findall(r'<link>(.*?)</link>',arguardian[i])
    
    title=re.findall(r'<title>(.*?)</title>',arguardian[i])
    try:
      picture[0]=picture[0].replace("amp;","")
      data[str(i)]={"link":link[0],"img":picture[0],"title":title[0].replace(u"\xa0"," ")}
    except:
      data[str(i)]={"link":link[0],"img":"","title":title[0].replace(u"\xa0"," ")}

  return data

def TheNewYorkTimesSC():
  TheNewYorkTimesSC=requests.get("https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml")
  s=TheNewYorkTimesSC.text
  s=s.replace("\n","")
  arnytimes=re.findall(r'<item>(.*?)</item>',s)
  data={}
  for i in range(len(arnytimes)):
    picture=re.findall(r'<media:content url="(.*?)"',arnytimes[i])
    link=re.findall(r'<link>(.*?)</link>',arnytimes[i])
    title=re.findall(r'<title>(.*?)</title>',arnytimes[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0],"title":title[0].replace(u"\xa0"," ")}
    except:
      data[str(i)]={"link":link[0],"img":"","title":title[0].replace(u"\xa0"," ")}

  return data

