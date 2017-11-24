from date_sales_num import process

json_string     = [[2017,2,0,346],[2017,3,0,347],[2017,4,0,348],[2017,5,1,349],[2017,6,2,350]]
date            = '2018,1,0'
res             = process(json_string, date)
print(res)