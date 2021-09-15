import flask
from flask import Flask, request
import json
from datetime import datetime
from flask_restful import Resource, Api
import sqlite3

app = Flask(__name__)
api = Api(app)


class IndexPage(Resource):
    @staticmethod
    def get():
        api_key = request.headers.get('X-API-KEY', default=1)
        con = sqlite3.connect('keys.db')
        cur = con.cursor()

        if api_key not in [key[0] for key in cur.execute("SELECT Key FROM Keys")]:
            obj = {"success": False, "reason": "Invalid api key"}
            response = app.response_class(
                response=json.dumps(obj),
                status=401,
                mimetype='application/json'
            )
            return response

        con.close()

        current_time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        ip = flask.request.remote_addr
        obj = {"success": True, "time": current_time, "ip": ip}
        response = app.response_class(
            response=json.dumps(obj),
            status=200,
            mimetype='application/json'
        )
        return response


api.add_resource(IndexPage, '/')

if __name__ == '__main__':
    app.run()
