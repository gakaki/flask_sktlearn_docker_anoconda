import requests
import ujson
json_data = {
    'series':      [[2017,2,0,346],[2017,3,0,347],[2017,4,0,348],[2017,5,1,349],[2017,6,2,350]],
    'next_date':   '2018,1,0',
}


r = requests.post('http://127.0.0.1:5000/data_sales_num', json=json_data)
print(r.text)
print(r.status_code)
print(ujson.dumps(json_data))
print(ujson.dumps(json_data['series']))
