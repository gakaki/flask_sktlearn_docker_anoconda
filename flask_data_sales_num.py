from flask import Flask, request, jsonify
from flask import render_template
from date_sales_num import process
import ujson
import time
import os

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__,template_folder=tmpl_dir)

#不写methods默认get
@app.route("/")
def hello():
    return "Flask Sales num by month regression!"

# http://127.0.0.1:5000/ajaxtest
@app.route('/ajaxtest')
def ajaxtest():
   return render_template('ajaxtest.html')

@app.route('/data_sales_num', methods=['POST'])
def data_sales_num():
   json_obj     = ujson.decode(request.form["json"])
   series       = json_obj['series']
   next_date    = json_obj["next_date"]
   print("--==== request series is ", series)
   print("--==== request next_date is ", next_date)

   series_str   = ujson.dumps(series)
   date_str     = next_date
   print('--==== start calc regression')

   start = time.clock()

   res_data     = process(series_str,date_str)

   end = time.clock()

   print('--==== end calc regression')

   print("--==== time elsaped %.2gs" % (end - start))

   return jsonify(res_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9999)

#using flask auto reload like php
#https://stackoverflow.com/questions/16344756/auto-reloading-python-flask-app-upon-code-changes