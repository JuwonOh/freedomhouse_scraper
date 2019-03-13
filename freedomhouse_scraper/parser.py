from .utils import get_soup
from .utils import now
from dateutil.parser import parse

def parse_page_blog(url):
    """
    Argument
    --------
    url : str
        Web page url

    Returns
    -------
    json_object : dict
        JSON format web page contents
        It consists with
            title : article title
            time : article written time
            content : text with line separator \\n
            url : web page url
            scrap_time : scrapped time
    """

    try:
        soup = get_soup(url)
        title = soup.find('h1', class_= 'title').text
        time = soup.find('div', class_= 'field field-name-post-date field-type-ds field-label-hidden').text
        content = soup.find('div', class_= 'field field-name-body field-type-text-with-summary field-label-hidden').text
        author = soup.find('p').text

        json_object = {
            'title' : title,
            'time' : parse(time),
            'content' : content,
            'url' : url,
            'author' : author,
            'scrap_time' : now()
        }
        return json_object
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None


def parse_page_news(url):
    """
    Argument
    --------
    url : str
        Web page url

    Returns
    -------
    json_object : dict
        JSON format web page contents
        It consists with
            title : article title
            time : article written time
            content : text with line separator \\n
            url : web page url
            scrap_time : scrapped time
    """

    try:
        soup = get_soup(url)
        title = soup.find('h1', class_= 'title').text
        time = soup.find('div', class_= 'field field-name-post-date field-type-ds field-label-hidden').text
        content = soup.find('div', class_= 'field field-name-body field-type-text-with-summary field-label-hidden').text

        json_object = {
            'title' : title,
            'time' : parse(time),
            'content' : content,
            'url' : url,
            'scrap_time' : now()
        }
        return json_object
    except Exception as e:
        print(e)
        print('Parsing error from {}'.format(url))
        return None
