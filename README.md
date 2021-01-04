# News-Scrapper
Web Scrapper for  news website get the headlines : https://pypi.org/project/newsscrapper-SamirPS/

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

The function return  a dict like {"1":{"link":X,"img":Y,"title":Z}}
