# freedomhouse_scraper

미국의 씽크탱크인(Freedom House)의 자료들(Blog, Press Release, initiatives)을 받아오기 위한 크롤러입니다.

## User guide

크롤러의 파이썬 파일은 util.py, scraper.py 그리고 parser.py 총 세가지로 구성되어 있습니다. 
util.py는 크롤링 한 파이썬의 beautifulsoup 패키지를 받아서 url내의 html정보를 정리합니다.
scraper는 util.py내의 사이트내의 url 링크들을 get_soup함수를 통해 모아줍니다.
parser는 이렇게 만들어진 url리스트를 통해서 각 분석들의 제목/일자/내용을 모아줍니다.

```
python scraping_latest_news.py
```

```
[1 / 50] (January 25, 2019) Angola: New Code Protects LGBTI Community 
[2 / 50] (January 18, 2019) DRC: African Union Intervenes to Defend Integrity of Presidential Election
[3 / 50] (January 15, 2019) Zimbabwe: Government Should Allow Protests, Re-Open Social Media
[4 / 50] (January 14, 2019) NGOs Urge US to Cooperate with UN Special Rapporteurs
[5 / 50] (January 2, 2019) South Africa Assumes Seat on UN Security Council  
[6 / 50] (December 20, 2018) Kazakhstan: Activists, Journalists Harassed on Independence Day
[7 / 50] (December 17, 2018) New Analyses Show Ongoing Russian Interference in US Democracy
[8 / 50] (December 13, 2018) U.S. Senate Condemns Saudi Crown Prince for Khashoggi Murder
[9 / 50] (December 13, 2018) Ethiopia: MCC Recognizes Opportunity for Democratic Reform
[10 / 50] (December 7, 2018) Crimea: Release Leading Attorney Detained on Trumped-Up Charges

Stop scrapping. 32 / 50 news was scrapped
The oldest news has been created after 2018-07-01
```

특정한 페이지를 parse하기 위해서는 usage파일을 참조하세요.

```
from freedomhouse_scraper import yield_latest_allblog

begin_date = '2018-07-01'
max_num = 50
sleep = 1.0

for i, json_obj in enumerate(yield_latest_allblog(begin_date, max_num, sleep)):
    title = json_obj['title']
    time = json_obj['time']
    print('[{} / {}] ({}) {}'.format(i+1, max_num, time, title))
```

## 참고 코드

본 코드는 https://github.com/lovit/whitehouse_scraper를 참조하여 만들어졌습니다.
