from flask import Flask
import json
from datetime import datetime
app = Flask(__name__)


@app.route('/time')
def return_time():
    current_time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    obj = {"time": current_time}
    response = app.response_class(
        response=json.dumps(obj),
        status=200,
        mimetype='application/json'
    )
    return response
