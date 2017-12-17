#!flask/bin/python
from flask import Flask
from dbconnector import set_keep_alive
import os
import time
import datetime
from datetime import timedelta

app = Flask(__name__)


def get_current_time():
    ts = time.time()
    if 'DYNO' not in os.environ:
        time_stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    else:
        time_stamp = (datetime.datetime.fromtimestamp(ts) + timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:%S')
    return time_stamp


@app.route('/')
def keep_alive():
    time_stamp = get_current_time()
    set_keep_alive(time_stamp)
    return '{} {}'.format(time_stamp, 'keep on keeping on')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)