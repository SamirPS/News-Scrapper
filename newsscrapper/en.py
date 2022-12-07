from utils import return_information


def CNNSC():
    return return_information(
        "http://rss.cnn.com/rss/edition",
        "item",
        "title",
        "link",
        "description",
        "media:content",
        "width",
        "height",
        "url",
    )


def FoxNewsSC():
    return return_information(
        "http://feeds.foxnews.com/foxnews/latest",
        "item",
        "title",
        "guid",
        "description",
        "media:content",
        "width",
        "height",
        "url",
    )


def ABCNewsSC():
    return return_information(
        "https://abcnews.go.com/abcnews/moneyheadlines",
        "item",
        "title",
        "link",
        "description",
        "media:thumbnail",
        "width",
        "height",
        "url",
    )


def TheGuardianSC():
    return return_information(
        "https://www.theguardian.com/us-news/rss",
        "item",
        "title",
        "guid",
        "description",
        "media:content",
        "width",
        "height",
        "url",
    )


def TheNewYorkTimesSC():
    return return_information(
        "https://www.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "item",
        "title",
        "link",
        "description",
        "media:content",
        "width",
        "height",
        "url",
    )
