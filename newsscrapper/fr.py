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

print(MondeSC())

def ParisSC():
  Paris=requests.get("https://www.leparisien.fr/arcio/sitemap/master/")
  arparis=re.findall(r'<loc>(.*?)</loc>',Paris.text)
  return arparis

def MediaPartSC():
  MediaPart=requests.get("https://www.mediapart.fr/articles/feed")
  armediapart=re.findall(r'<link>(.*?)</link>',MediaPart.text)
  del armediapart[0]
  return armediapart

def BmftvSC():
  Bfmtv=requests.get("https://www.bfmtv.com/rss/news-24-7/")
  arbfmtv=re.findall(r'<link>(.*?)</link>',Bfmtv.text)
  del arbfmtv[0]
  return arbfmtv

def LibeSC():
  Liberation=requests.get("http://rss.liberation.fr/rss/latest/")
  arlibe=re.findall(r'<link href="(.*?)"',Liberation.text)
  del arlibe[0]
  return arlibe

def FTISC():
  Francetvinfo=requests.get("https://www.francetvinfo.fr/titres.rss")
  arfti=re.findall(r'<link>(.*?)#',Francetvinfo.text)
  del arfti[0]
  return arfti





