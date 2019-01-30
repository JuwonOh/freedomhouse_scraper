import re
import time
from .parser import parse_page_news
from .parser import parse_page_blog
from .utils import get_soup
from .utils import news_dateformat
from .utils import user_dateformat
from .utils import strf_to_datetime

patterns = [
    re.compile('https://freedomhouse.org/[\w]+')]
url_blogbase = 'https://freedomhouse.org/blog?page={}'

def yield_latest_allblog(begin_date, max_num=10, sleep=1.0):
    """
    Artuments
    ---------
    begin_date : str
        eg. 2018-01-01
    max_num : int
        Maximum number of news to be scraped
    sleep : float
        Sleep time. Default 1.0 sec

    It yields
    ---------
    news : json object
    """

    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get urls
        links_all = []
        url = url_blogbase.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('h2', class_= 'node-title')
        links = ['https://freedomhouse.org' + i.find('a')['href'] for i in sub_links]
        links_all += links

        # scrap
        for url in links_all:

            news_json = parse_page_blog(url)

            # check date
            d_news = strf_to_datetime(news_json['time'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

def get_allblog_urls(begin_page=0, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 0
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_blogbase.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('h2', class_= 'node-title')
        links = ['https://freedomhouse.org' + i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))
    return links_all

def get_last_blogpage_num():
    """
    Returns
    -------
    page : int
        Last page number.
        eg: 13 in 'https://freedomhouse.org/blog?page=76'
    """
    last_page = []

    soup = get_soup('https://freedomhouse.org/blog?page=1')
    last_page = soup.find('a', title='Go to last page')['href']
    last_page = ['https://freedomhouse.org' + i for i in last_page]
    return last_page

url_PRbase = 'https://freedomhouse.org/news/press-releases?page={}'


def yield_latest_pr(begin_date, max_num=50, sleep=1.0):
    """
    Artuments
    ---------
    begin_date : str
        eg. 2018-01-01
    max_num : int
        Maximum number of news to be scraped
    sleep : float
        Sleep time. Default 1.0 sec

    It yields
    ---------
    news : json object
    """

    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        #get PR_urls
        links_PR = []
        url = url_PRbase.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('h2', class_= 'node-title')
        links = ['https://freedomhouse.org' + i.find('a')['href'] for i in sub_links]
        links_PR += links

        # scrap
        for url in links_PR:
            news_json = parse_page_news(url)
            # check date
            d_news = strf_to_datetime(news_json['time'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

            # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)

def get_PR_urls(begin_page=0, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []
    for page in range(begin_page, end_page+1):
        url = url_PRbase.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('h2', class_= 'node-title')
        links = ['https://freedomhouse.org' + i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))
    return links_all

def get_last_PR_num():
    """
    Returns
    -------
    page : int
        Last page number.
        eg: 13 in 'https://freedomhouse.org/news/press-releases?page=267'
    """
    last_page = []

    soup = get_soup('https://freedomhouse.org/news/press-releases?page=21')
    last_page_list = soup.find_all('li', class_ = 'pager-last last')
    last_page = [i.find('a')['href'] for i in last_page_list]
    last_page = ['https://freedomhouse.org' + i for i in last_page]
    return last_page

url_initbase = 'https://freedomhouse.org/initiatives?page={}'


def yield_latest_init(begin_date, max_num=50, sleep=1.0):
    """
    Artuments
    ---------
    begin_date : str
        eg. 2018-01-01
    max_num : int
        Maximum number of news to be scraped
    sleep : float
        Sleep time. Default 1.0 sec

    It yields
    ---------
    news : json object
    """

    # prepare parameters
    d_begin = strf_to_datetime(begin_date, user_dateformat)
    end_page = 72
    n_news = 0
    outdate = False

    for page in range(0, end_page+1):

        # check number of scraped news
        if n_news >= max_num or outdate:
            break

        # get init_urls
        links_init = []
        url = url_initbase.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('h2', class_= 'node-title')
        links = ['https://freedomhouse.org' + i.find('a')['href'] for i in sub_links]
        links_init += links

        # scrap
        for url in links_init:
            news_json = parse_page_news(url)
            # check date
            d_news = strf_to_datetime(news_json['time'], news_dateformat)
            if d_begin > d_news:
                outdate = True
                print('Stop scrapping. {} / {} news was scrapped'.format(n_news, max_num))
                print('The oldest news has been created after {}'.format(begin_date))
                break

            # yield
            yield news_json

            # check number of scraped news
            n_news += 1
            if n_news >= max_num:
                break
            time.sleep(sleep)

def get_allinit_urls(begin_page=0, end_page=3, verbose=True):
    """
    Arguments
    ---------
    begin_page : int
        Default is 1
    end_page : int
        Default is 3
    verbose : Boolean
        If True, print current status

    Returns
    -------
    links_all : list of str
        List of urls
    """

    links_all = []

    for page in range(begin_page, end_page+1):
        url = url_initbase.format(page)
        soup = get_soup(url)
        sub_links = soup.find_all('h2', class_= 'node-title')
        links = ['https://freedomhouse.org' + i.find('a')['href'] for i in sub_links]
        links_all += links
        if verbose:
            print('get briefing statement urls {} / {}'.format(page, end_page))
    return links_all


def get_last_init_num():
    """
    Returns
    -------
    page : int
        Last page number.
        eg: 13 in 'https://freedomhouse.org/initiatives?page=35'
    """
    last_page = []

    soup = get_soup('https://freedomhouse.org/initiatives')
    last_page_list = soup.find_all('li', class_ = 'pager-last last')
    last_page = [i.find('a')['href'] for i in last_page_list]
    last_page = ['https://freedomhouse.org' + i for i in last_page]
    return last_page
