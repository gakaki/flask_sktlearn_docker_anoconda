from flask import Flask, request, jsonify
from date_sales_num import process
import ujson
import time

app = Flask(__name__)

#不写methods默认get
@app.route("/")
def hello():
    return "Flask Sales num by month regression!"

@app.route('/data_sales_num', methods=['POST'])
def data_sales_num():
   data         = request.get_json()
   print("--==== request json is ", data)

   series_str   = ujson.dumps(data['series'])
   date_str     = data['next_date']
   print("--==== input params is ",series_str,date_str)

   print('--==== start calc regression')

   start = time.clock()

   res_data     = process(series_str,date_str)

   end = time.clock()

   print('--==== end calc regression')

   print("--==== time elsaped %.2gs" % (end - start))

   return jsonify(res_data)

if __name__ == '__main__':
    app.run(debug=True)

#using flask auto reload like php
#https://stackoverflow.com/questions/16344756/auto-reloading-python-flask-app-upon-code-changes