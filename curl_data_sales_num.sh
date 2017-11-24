#!/usr/bin/env bash
curl -H "Content-Type: application/json" -d '{"series":[[2017,2,0,346],[2017,3,0,347],[2017,4,0,348],[2017,5,1,349],[2017,6,2,350]],"next_date":"2018,1,0"}' http://127.0.0.1:5000/data_sales_num
