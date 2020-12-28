import requests
import re

Monde=requests.get("https://www.lemonde.fr/rss/une.xml")
armonde=re.findall(r'<link>(.*?)</link>',Monde.text)
del armonde[0]
print(armonde)

Paris=requests.get("https://www.leparisien.fr/arcio/sitemap/master/")
arparis=re.findall(r'<loc>(.*?)</loc>',Paris.text)
del arparis[0]
print(arparis)

MediaPart=requests.get("https://www.mediapart.fr/articles/feed")
armediapart=re.findall(r'<link>(.*?)</link>',MediaPart.text)
del armediapart[0]
print(armediapart)

Bfmtv=requests.get("https://www.bfmtv.com/rss/news-24-7/")
arbfmtv=re.findall(r'<link>(.*?)</link>',Bfmtv.text)
del arbfmtv[0]
print(arbfmtv)

Liberation=requests.get("http://rss.liberation.fr/rss/latest/")
arlibe=re.findall(r'<link href="(.*?)"',Liberation.text)
del arlibe[0]
print(arlibe)




