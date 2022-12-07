from utils import return_information


def MondeSC():
    return return_information(
        "https://www.lemonde.fr/rss/une.xml",
        "item",
        "title",
        "link",
        "description",
        "media:content",
        "width",
        "height",
        "url",
    )


def MediaPartSC():
    return return_information(
        "https://www.mediapart.fr/articles/feed",
        "item",
        "title",
        "link",
        "description",
        "media:content",
        "width",
        "height",
        "url",
    )


def BmftvSC():
    return return_information(
        "https://www.bfmtv.com/rss/news-24-7/",
        "item",
        "title",
        "link",
        "description",
        "enclosure",
        "width",
        "height",
        "url",
    )


def LibeSC():
    return return_information(
        "https://www.liberation.fr/arc/outboundfeeds/rss/?outputType=xml",
        "item",
        "title",
        "link",
        "description",
        "media:content",
        "width",
        "height",
        "url",
    )
