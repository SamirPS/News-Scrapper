# News-Scrapper

![PyPI](https://img.shields.io/pypi/v/newsscrapper-SamirPS)

Web Scrapper for gettings the headlines of some news websites:
https://pypi.org/project/newsscrapper-SamirPS/

To import the function :
## FR:
```python
from newsscrapper import fr
```
* LeMonde : fr.MondeSC()
* MediaPart: fr.MediaPartSC()
* BFMTV : fr.BmftvSC()
* Libération : fr.LibeSC()


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
* ELPAIS: es.ELPAISSC()

The function return a dict like {"1":{"link":A,"images":{key_image:B,...},"title":C,"description":D,"summary":E}}

The ... is for multiple images; key_image can be the "heightxweight" of the picture or a string representing an integer if we don't have the height or weight.
