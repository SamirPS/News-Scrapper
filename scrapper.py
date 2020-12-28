import requests
import re

def MondeSC():
  Monde=requests.get("https://www.lemonde.fr/rss/une.xml")
  armonde=re.findall(r'<link>(.*?)</link>',Monde.text)
  return armonde

def ParisSC():
  Paris=requests.get("https://www.leparisien.fr/arcio/sitemap/master/")
  arparis=re.findall(r'<loc>(.*?)</loc>',Paris.text)
  return arparis

def MediaPartSC():
  MediaPart=requests.get("https://www.mediapart.fr/articles/feed")
  armediapart=re.findall(r'<link>(.*?)</link>',MediaPart.text)
  return armediapart

def BmftvSC():
  Bfmtv=requests.get("https://www.bfmtv.com/rss/news-24-7/")
  arbfmtv=re.findall(r'<link>(.*?)</link>',Bfmtv.text)
  return arbfmtv

def LibeSC():
  Liberation=requests.get("http://rss.liberation.fr/rss/latest/")
  arlibe=re.findall(r'<link href="(.*?)"',Liberation.text)
  return arlibe

def FTISC():
  Francetvinfo=requests.get("https://www.francetvinfo.fr/titres.rss")
  arfti=re.findall(r'<link>(.*?)#',Francetvinfo.text)
  return arfti





