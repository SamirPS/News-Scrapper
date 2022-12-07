from bs4 import BeautifulSoup
import requests


def return_information(
    url: str,
    tag_article: str,
    tag_title: str,
    tag_link: str,
    tag_description: str,
    tag_image: str,
    tag_image_h: str,
    tag_image_w: str,
    tag_image_link: str,
):
    website = requests.get(url)
    data = {}
    content = website.content
    soup = BeautifulSoup(content, "xml")
    items = soup.find_all(tag_article)
    for count, item in enumerate(items):

        try:
            title = item.find(tag_title).text
        except AttributeError:
            title = None

        try:
            link = item.find(tag_link).text
        except AttributeError:
            link = None

        try:
            description = item.find(tag_description).text
        except AttributeError:
            description = None

        images = {}
        for count_image, image in enumerate(item.find_all(tag_image)):
            try:
                h = image.get(tag_image_h)
                w = image.get(tag_image_w)
                if h is None or w is None:
                    key = count_image
                else:
                    key = f"{h}x{w}"
                link_image = image.get(tag_image_link)
                images[key] = link_image
            except Exception:
                pass

        data[f"{count}"] = {
            "link": link,
            "images": images,
            "title": title,
            "description": description,
        }

    return data
