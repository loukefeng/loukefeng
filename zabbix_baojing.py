import json
import requests
import sys
def mas(url,remiders,mag):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",
        "at":{
            "atMobiles": remiders,
            "isAtAll":False,

        },
        "text":{
            "content": mag,
        }
    }
    r = requests.post(url,headers=headers,data=json.dumps(data))
    return r.text
if __name__ == '__main__':
    mag =sys.argv[1]
    remiders = []
    url = '钉钉机器人url'
    print(mas(url,remiders,mag))