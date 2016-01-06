from flask import Flask, make_response, request
from flask.ext.cors import cross_origin
import json
from time import sleep


app = Flask(__name__)

@app.route("/search/:query")
@cross_origin()
def search(query):
    # TODO create some file with data to search from
    return query

@app.route("/contest/", methods=['POST', 'OPTIONS'])
@cross_origin(allow_headers=['Content-Type'])
def post_contest_data():
    # do something with posted data
    contest_data = request.get_json()
    sleep(1) # sleep to slow things down
    print(contest_data)
    return "Done"

if __name__ == "__main__":
    app.run(port=2137) # localhost