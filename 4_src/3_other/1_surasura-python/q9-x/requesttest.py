import requests

dat = requests.get('https://pycon.jp/2016/ja/schedule/talks/list/').text
print(dat)