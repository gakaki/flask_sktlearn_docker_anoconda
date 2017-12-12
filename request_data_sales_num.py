import requests
import ujson
json_data = {
    'series':      [[2017,1,1655],[2017,2,963],[2017,3,1468],[2017,4,1269],[2017,5,1690],[2017,6,1706],[2017,7,1589],[2017,8,1931],[2017,9,2094]],
    "next_date":   '2017,10'
    # 'series': [['2017', '2', '0', '346'], ['2017', '3', '0', '347'], ['2017', '4', '0', '348'],
    #            ['2017', '5', '1', '349'], ['2017', '6', '2', '350']],
    # 'next_date':   '2018,1,0',
}
data = {
    'json' : ujson.encode(json_data)
}
# {"series":[[2017,1,1655],[2017,2,963],[2017,3,1468],[2017,4,1269],[2017,5,1690],[2017,6,1706],[2017,7,1589],[2017,8,1931],[2017,9,2094]],"next_date":[2017,10]}

# r = requests.post('http://127.0.0.1:5000/data_sales_num', json = json_data)
r = requests.post('http://192.168.2.126:9999/data_sales_num', data = data)
print(r.text)
print(r.status_code)
print(ujson.dumps(json_data))
print(ujson.dumps(json_data['series']))
