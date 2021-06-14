import requests
import re

def MondeSC():
  Monde=requests.get("https://www.lemonde.fr/rss/une.xml")
  armonde=re.findall(r'<item>(.*?)</item>',Monde.text)
  data={}
  for i in range(len(armonde)):
    picture=re.findall(r'<media:content url="(.*?)"',armonde[i])
    link=re.findall(r'<link>(.*?)</link>',armonde[i])
    title=re.findall(r'<title><!\[CDATA\[(.*?)]]>',armonde[i])
    try:
      data[str(i)]={"link":link[0],"img":picture[0],"title":title[0].replace(u"\xa0"," ")}
    except:
      data[str(i)]={"link":link[0],"img":"","title":title[0].replace(u"\xa0"," ")}

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
    title=link[0].split("/")
    titre=title[-1].split("-")
    fini=" ".join(titre[0:len(titre)-4]) 
    try:
      data[str(i)]={"link":link[0],"img":picture[0],"title":fini}
    except:
      data[str(i)]={"link":link[0],"img":"","title":fini}
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
    title=re.findall(r'<title><!\[CDATA\[(.*?)]]>',armediapart[i])

    try:
      data[str(i)]={"link":link[0],"img":picture[0],"title":title[0].replace(u"\xa0"," ")}
    except:
      data[str(i)]={"link":link[0],"img":"","title":title[0].replace(u"\xa0"," ")}
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
    title=re.findall(r'<title><!\[CDATA\[(.*?)]]>',arbfmtv[i])

    try:
      data[str(i)]={"link":link[0],"img":picture[0],"title":title[0].replace(u"\xa0"," ")}
    except:
      data[str(i)]={"link":link[0],"img":"","title":title[0].replace(u"\xa0"," ")}
  return data


def LibeSC():
  Liberation=requests.get("https://www.liberation.fr/arc/outboundfeeds/rss/?outputType=xml")
  s=Liberation.text
  s=s.replace("\n","")
  arlibe=re.findall(r'<item>(.*?)</item>',s)
  data={}
  for i in range(len(arlibe)):
    picture=re.findall(r'https://liberation-liberation-prod.cdn.arcpublishing.com/resizer/(.*?)">',arlibe[i])
    link=re.findall(r'<link>(.*?)</link>',arlibe[i])
    title=re.findall(r'<title>(.*?)</title>',arlibe[i])
    title[0]=title[0].replace("<![CDATA[","").replace("]]>","")
    addj="https://liberation-liberation-prod.cdn.arcpublishing.com/resizer/"
    try:
      data[str(i)]={"link":link[0],"img":addj+picture[0],"title":title[0].replace(u"\xa0"," ")}
    except:
      data[str(i)]={"link":link[0],"img":"","title":title[0].replace(u"\xa0"," ")}
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
    title=re.findall(r'<title>(.*?)</title>',arfti[i])

    try:
      data[str(i)]={"link":link[0],"img":picture[0],"title":title[0].replace(u"\xa0"," ")}
    except:
      data[str(i)]={"link":link[0],"img":"","title":title[0].replace(u"\xa0"," ")}
  return data






