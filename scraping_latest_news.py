import argparse
import json
import os
import re
from freedomhouse_scraper import yield_latest_allblog
from freedomhouse_scraper import yield_latest_pr
from freedomhouse_scraper import yield_latest_init

def save(json_obj, directory):
    url = json_obj['url']
    title = [p for p in url.split('/') if p][-1]
    category = [p for p in url.split('/') if p][-2]
    dt = json_obj['time']  
    name = '{}-{}-{}_{}_{}'.format(dt.year, dt.month, dt.day, category, re.sub("[\/:*?\<>|]","", title[:50]))
    filepath = '{}/{}.json'.format(directory, name)
    with open(filepath, 'w', encoding='utf-8') as fp:
        json.dump(json_obj, fp, indent=2, ensure_ascii=False, sort_keys=True, default=str)

def scraping(begin_date, max_num, sleep, directory, verbose):

    n_exceptions = 0
# blog category
    for i, json_obj in enumerate(yield_latest_allblog(begin_date, max_num, sleep)):
        try:
            save(json_obj, directory)
        except Exception as e:
            n_exceptions += 1
            print(e)
            continue

        if verbose:
            title = json_obj['title']
            time = json_obj['time']
            print('[{} / {}] ({}) {}'.format(i+1, max_num, time, title))

    if n_exceptions > 0:
        print('Exist %d security exceptions' % n_exceptions)
# initiatives category
    for i, json_obj in enumerate(yield_latest_init(begin_date, max_num, sleep)):
        try:
            save(json_obj, directory)
        except Exception as e:
            n_exceptions += 1
            print(e)
            continue

        if verbose:
            title = json_obj['title']
            time = json_obj['time']
            print('[{} / {}] ({}) {}'.format(i+1, max_num, time, title))

    if n_exceptions > 0:
        print('Exist %d people exceptions ' % n_exceptions)
# press releases category
    for i, json_obj in enumerate(yield_latest_pr(begin_date, max_num, sleep)):
        try:
            save(json_obj, directory)
        except Exception as e:
            n_exceptions += 1
            print(e)
            continue

        if verbose:
            title = json_obj['title']
            time = json_obj['time']
            print('[{} / {}] ({}) {}'.format(i+1, max_num, time, title))

    if n_exceptions > 0:
        print('Exist %d pivot exceptions' % n_exceptions)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--begin_date', type=str, default='2018-07-01', help='datetime YYYY-mm-dd')
    parser.add_argument('--directory', type=str, default='./output/', help='Output directory')
    parser.add_argument('--max_num', type=int, default=1000, help='Maximum number of news to be scraped')
    parser.add_argument('--sleep', type=float, default=1.0, help='Sleep time for each news')
    parser.add_argument('--verbose', dest='VERBOSE', action='store_true')

    args = parser.parse_args()
    begin_date = args.begin_date
    directory = args.directory
    max_num = args.max_num
    sleep = args.sleep
    VERBOSE = args.VERBOSE

    # check output directory
    if not os.path.exists(directory):
        os.makedirs(directory)

    scraping(begin_date, max_num, sleep, directory, VERBOSE)

if __name__ == '__main__':
    main()
