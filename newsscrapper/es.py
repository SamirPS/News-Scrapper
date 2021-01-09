import requests
import re

def ELPAISSC():
  ELPAIS=requests.get("http://ep00.epimg.net/rss/tags/ultimas_noticias.xml")
  s=ELPAIS.text.replace("\n",'')
  arelpais=re.findall(r'<item>(.*?)</item>',s)
  data={}
  for i in range(len(arelpais)):
    
    picture=re.findall(r'<enclosure url="(.*?)" length',arelpais[i])
    link=re.findall(r'<link><!\[CDATA\[(.*?)]]>',arelpais[i])
    title=re.findall(r'<title><!\[CDATA\[(.*?)]]>',arelpais[i])

    try:
      data[str(i)]={"link":link[0],"img":picture[0],"title":title[0].replace(u"\xa0"," ")}
    except:
      data[str(i)]={"link":link[0],"img":"","title":title[0].replace(u"\xa0"," ")}

  return data

def EFESC():
  EFE=requests.get("https://www.efe.com/efe/espana/1/rss")
  s=EFE.text.replace("\n",'')
  arefe=re.findall(r'<item>(.*?)</item>',s)
  data={}
  for i in range(len(arefe)):
    
    picture=re.findall(r'<enclosure url="(.*?)" length',arefe[i])
    link=re.findall(r'<link>(.*?)?utm_source',arefe[i])
    title=re.findall(r'<title>(.*?)</title>',arefe[i])

    try:
      data[str(i)]={"link":link[0],"img":picture[0],"title":title[0].replace(u"\xa0"," ")}
    except:
      data[str(i)]={"link":link[0],"img":"","title":title[0].replace(u"\xa0"," ")}

  return data

