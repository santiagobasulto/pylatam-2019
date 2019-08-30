import time
import json
import sqlite3
from flask import Flask, g

app = Flask(__name__)


@app.before_request
def before_request():
    g.db = sqlite3.connect('prices.db')


@app.teardown_request
def teardown_request_func(error=None):
    g.db.close()


HELP_MESSAGE = """
Docs:
    * /exchanges
    * /symbols
    * /price/{exchange}/{symbol}/{date}
        date: '2018-12-31'
"""

@app.route('/')
def index():
    return HELP_MESSAGE, 200, {'Content-Type': 'text/plain'}


@app.route('/exchanges')
def exchanges():
    cursor = g.db.execute("SELECT DISTINCT exchange FROM price;")
    results = cursor.fetchall()
    exchanges = [exc for sub in results for exc in sub]
    return json.dumps(exchanges), 200, {'Content-Type': 'application/json'}


@app.route('/symbols')
def symbols():
    cursor = g.db.execute("SELECT DISTINCT symbol FROM price;")
    results = cursor.fetchall()
    symbols = [exc for sub in results for exc in sub]
    return json.dumps(symbols), 200, {'Content-Type': 'application/json'}


@app.route('/price/<exchange>/<symbol>/<date>')
def price(exchange, symbol, date):
    time.sleep(.2)
    g.db.row_factory = sqlite3.Row
    cursor = g.db.execute("""
        SELECT exchange, symbol, open, high, low, close, volume, day FROM price
        WHERE exchange = ? AND symbol = ? AND day = ?;
    """, (exchange, symbol, date))
    results = [dict(r) for r in cursor.fetchall()]
    result = None
    if len(results):
        result = results[0]
    return json.dumps(result), 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.debug = True
    app.run()