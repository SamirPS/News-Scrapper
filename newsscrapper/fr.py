import requests
import re

def MondeSC():
  Monde=requests.get("https://www.lemonde.fr/rss/une.xml")
  armonde=re.findall(r'<item>(.*?)</item>',Monde.text)
  data={}
  for i in range(len(armonde)):
    picture=re.findall(r'<media:content url="(.*?)"',armonde[i])
    link=re.findall(r'<link>(.*?)</link>',armonde[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0]}
    except:
      data[str(i)]={"link":link[0],"img":""}

  return data


def ParisSC():
  Paris=requests.get("https://www.leparisien.fr/arcio/sitemap/master/")
  
  s=Paris.text
  s=s.replace("\n","")
  arparis=re.findall(r'<url>(.*?)</url>',s)
  data={}
  for i in range(len(arparis)):
    picture=re.findall(r'<image:loc>(.*?)</image:loc>',arparis[i])
    link=re.findall(r'<loc>(.*?)</loc>',arparis[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0]}
    except:
      data[str(i)]={"link":link[0],"img":""}
  return data


def MediaPartSC():
  MediaPart=requests.get("https://www.mediapart.fr/articles/feed")
  s=MediaPart.text
  s=s.replace("\n","")
  armediapart=re.findall(r'<item>(.*?)</item>',s)
  data={}
  for i in range(len(armediapart)):
    picture=re.findall(r'<media:content url="(.*?)"',armediapart[i])
    link=re.findall(r'<link>(.*?)</link>',armediapart[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0]}
    except:
      data[str(i)]={"link":link[0],"img":""}
  return data
  


def BmftvSC():
  Bfmtv=requests.get("https://www.bfmtv.com/rss/news-24-7/")
  s=Bfmtv.text
  s=s.replace("\n","")
  arbfmtv=re.findall(r'<item>(.*?)</item>',s)
  data={}
  for i in range(len(arbfmtv)):
    picture=re.findall(r'<enclosure url="(.*?)"',arbfmtv[i])
    link=re.findall(r'<link>(.*?)</link>',arbfmtv[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0]}
    except:
      data[str(i)]={"link":link[0],"img":""}
  return data
  

def LibeSC():
  Liberation=requests.get("http://rss.liberation.fr/rss/latest/")
  s=Liberation.text
  s=s.replace("\n","")
  arlibe=re.findall(r'<entry>(.*?)</entry>',s)
  data={}
  for i in range(len(arlibe)):
    picture=re.findall(r'https://medias.liberation.fr/photo/(.*?);ratio',arlibe[i])
    link=re.findall(r'<link href="(.*?)"',arlibe[i])
    try:
      data[str(i)]={"link":link[0],"img":"https://medias.liberation.fr/photo/"+picture[0]}
    except:
      data[str(i)]={"link":link[0],"img":""}
  return data

def FTISC():
  Francetvinfo=requests.get("https://www.francetvinfo.fr/titres.rss")
  s=Francetvinfo.text
  s=s.replace("\n","")
  arfti=re.findall('<item>(.*?)</item>',s)
  data={}
  for i in range(len(arfti)):
    picture=re.findall(r'url="(.*?)"',arfti[i])
    link=re.findall(r'<link>(.*?)</link>',arfti[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0]}
    except:
      data[str(i)]={"link":link[0],"img":""}

  return data






