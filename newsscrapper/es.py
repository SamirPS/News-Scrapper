from utils import return_information


def ELPAISSC():
    return return_information(
        "https://feeds.elpais.com/mrss-s/pages/ep/site/elpais.com/portada",
        "item",
        "title",
        "link",
        "description",
        "media:content",
        "width",
        "height",
        "url",
    )
