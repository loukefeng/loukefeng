import requests
import json

url = 'http://192.168.4.10/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# 4817180d836aba422580cd927b175704
#
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             # "host": [
#             #     "Zabbix server",
#             #     "Linux server"
#             # ]
#         }
#     },
#     "auth": "4817180d836aba422580cd927b175704",
#     "id": 1
# }
# data ={
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10084"
#     ],
#     "auth": "4817180d836aba422580cd927b175704",
#     "id": 1
# }
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "4817180d836aba422580cd927b175704",
#     "id": 1
# }
# group_id :2
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#                 "Template OS Windows"
#             ]
#         }
#     },
#     "auth": "4817180d836aba422580cd927b175704",
#     "id": 1
# }
# templateid': '10081
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "Linux server",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.10",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10081"
            }
        ],
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "4817180d836aba422580cd927b175704",
    "id": 1
}
r = requests.post(url,headers=headers,data=json.dumps(data))
print(r.json())