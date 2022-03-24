## Instagram Insights
- Reach refers to the total number of unique accounts that have seen your post or story. 
- Impressions measure the total number of times users saw your post or story.


## 参加募集要項
~~~
3年生の皆さんへ
データサイエンス研究構想コンテストの参加登録締切は10月11日（月）です。
3年生は全員参加を予定しています。
参加登録の際には、500文字程度の研究構想に関する要約文が必要です。
個人またはグループで話し合って要約文を作成して、10/9（土）までに私に提出してください。
----------------------
開催日		2021年10月23日（土）... 開会式、ポスタープレビュー、ポスター発表
		　　2021年10月24日（日）... 学長特別講演、表彰式、閉会式
参加資格　　　　本学の学部生、大学院生
参加登録締切　	10月11日（月）まで
賞		　　　最優秀賞、データ解析賞、データ活用賞、奨励賞、ポスター賞を選出
ホームページ	https://www.ads.tuis.ac.jp/competition/2021/
参加登録ページ	https://forms.office.com/r/LCpDXSbbPk
~~~

## Follow and Unfollow
- Write down all the number

## Insta-scrape (X)dont use this
- [Instascrape](https://dev.to/chrisgreening/visualizing-instagram-engagement-with-instascrape-326h)○
- need to provide session ID to login (44963294170%3ATMogQdGgK7Et3m%3A3)
- Example to start
~~~
from instascrape import *
session_id = '44963294170%3ATMogQdGgK7Et3m%3A3' # Your session ID - http://valvepress.com/how-to-get-instagram-session-cookie/
google = Profile('https://www.instagram.com/google/')
headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57","cookie": f"sessionid={session_id};"}
google.scrape(headers=headers)
print(google.followers)
~~~
- [Documentation](https://instascrape.readthedocs.io/en/latest/instascrape.scrapers.html#instascrape.scrapers.profile.Profile.get_posts)


## Instagram Loader
- [Instagram Engagement Rate](https://kevinjnguyen.medium.com/using-python-to-calculate-instagram-engagement-percentage-subtle-clothing-collection-99284dc750c2)
- [Documentation](https://instaloader.github.io/basic-usage.html#metadata-text-files)


## Useful Link
- [Pandas](https://youtu.be/vmEHCJofslg) x
- [Restaurant Data Analysis](https://www.kaggle.com/ankitantony/mexico-restaurant-data-analysis-using-python)
- [Instagram API](https://www.kdnuggets.com/2017/08/instagram-python-data-analysis.html) x
- [Beginner Guide To Data Analysis](https://towardsdatascience.com/a-beginners-guide-to-data-analysis-in-python-188706df5447)  
- [Blob City ML](https://cloud.blobcity.com/code/explore)

## Account for U REJI
- UレジFood
- 企業コード：501449 
- コード：101
- PSD：masak202000

## FIle
All file need to transform into UTF-8