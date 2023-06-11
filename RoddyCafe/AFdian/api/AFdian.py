import requests
import json

from datetime import datetime, timedelta

headers = {
        'authority' : 'afdian.net',
        'accept' : 'application/json,text/plain,*/*',
        'accept-language' : 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ko;q=0.6',
        'locale-lang' : 'zh-CN',
        'sec-ch-ua' : '\"GoogleChrome\";v=\"113\",\"Chromium\";v=\"113\",\"Not-A.Brand\";v=\"24\"',
        'sec-ch-ua-mobile' : '?0',
        'sec-ch-ua-platform' : '\"Windows\"',
        'sec-fetch-dest' : 'empty',
        'sec-fetch-mode' : 'cors',
        'sec-fetch-site' : 'same-origin',
        'user-agent' : 'Mozilla/5.0(WindowsNT10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/113.0.0.0Safari/537.36',
    }

def get_sponsorships(auth_token):
    headers["cookie"] = "auth_token=" + auth_token
    response = requests.get(
        "https://afdian.net/api/my/profile", 
        headers=headers
    ).content.decode('utf-8')
    if json.loads(response)["ec"] != 200: return None, 502
    page = 1
    response = requests.get(
        "https://afdian.net/api/my/sponsored-bill-filter?" + "&page=" + str(page), 
        headers=headers
    ).content.decode('utf-8')
    sponsorships = []
    while(json.loads(response)["data"]["has_more"]):
        for s in json.loads(response)["data"]["list"]:
            sponsorships.append(s)
        page += 1
        response = requests.get(
            "https://afdian.net/api/my/sponsored-bill-filter?" + "&page=" + str(page), 
            headers=headers
        ).content.decode('utf-8')
    for s in json.loads(response)["data"]["list"]:
        start_year = int(s['out_trade_no'][0:4])
        start_month = int(s['out_trade_no'][4:6])
        start_day = int(s['out_trade_no'][6:8])
        duration_seconds = int(s['time_range']['end_time']) - int(s['time_range']['begin_time'])
        expire_day = datetime(start_year, start_month, start_day) + timedelta(seconds=duration_seconds)
        interval = datetime.now() - expire_day
        if interval.days <= 30: sponsorships.append(s)
    if sponsorships: return sponsorships, 200
    else: return None, 404