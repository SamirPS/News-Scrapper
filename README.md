# News-Scrapper
Web Scrapper for  news website get the headlines : https://pypi.org/project/newsscrapper-SamirPS/
POC : https://newswebs.herokuapp.com/
TODO: Get the title of the article
      Get the description of the article
To import the function :
## FR:
```python
from newsscrapper import fr
```
* LeMonde : fr.MondeSC()
* LeParisien: fr.ParisSC()
* MediaPart: fr.MediaPartSC()
* BFMTV : fr.BmftvSC()
* Libération : fr.LibeSC()
* FranceTv INFO : fr.LibeSC()


## EN:
```python
from newsscrapper import en
```
* CNN :  en.CNNSC()
* FoxNews: en.FoxNewsSC()
* AbcNews: en.ABCNewsSC()
* TheGuardian : en.TheGuardianSC()
* TheNewYorkTimes : en.TheNewYorkTimesSC()


## ES:
```python
from newsscrapper import es
```
* EFE :  es.EFESC()
* ELPAIS: es.ELPAISSC()

The function return  a dict like {"1":{"link":X,"img":Y,"title":Z}}
