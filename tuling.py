import json
import requests

def reply(url,apikey,mag):
    data = {
	"reqType":0,
    "perception": {
        "inputText": {
            "text": mag
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": "北京",
                "province": "北京",
                "street": "信息路"
            }
        }
    },
    "userInfo": {
        "apiKey": apikey,
        "userId": 'anystr'
    }
}
    headers = {'content-type': 'application/json'}
    r = requests.post(url,headers=headers,data=json.dumps(data))
    return r.json()
if __name__ == '__main__':
    apikey = '3a481ce9137846c18707fd802a09586a'
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    while True:
        mag = input('(输入quit结束)> ').strip()
        if not mag:
            continue
        if mag == 'quit':
            break
        reply1 = reply(url,apikey,mag)
        print(reply1['results'][0]['values']['text'])