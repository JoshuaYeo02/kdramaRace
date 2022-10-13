from flask import *
import json, time

from kdramaAPIUtils import search_func, fetch_func

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home_page():
    data_set = {'Page': 'home', 'message': 'kdrama api', 'time' : time.time()}
    json_dump = json.dumps(data_set, indent=4, sort_keys=True, default=str)

    return json_dump

@app.route('/people/', methods = ['GET'])
def fetch_people():
    people = str(request.args.get('people'))
    
    data_set = fetch_func(query=f"people/{people}", t="person")
    json_dump = json.dumps(data_set, indent=4, sort_keys=True, default=str)

    return json_dump


@app.route('/cast/', methods = ['GET'])
def fetch_cast():
    cast = str(request.args.get('cast')) 

    data_set = fetch_func(query=f"{cast}/cast", t="cast")
    json_dump = json.dumps(data_set, indent=4, sort_keys=True, default=str)

    return json_dump

@app.route('/id/', methods = ['GET'])
def fetch_drama():
    id = str(request.args.get('id')) 

    data_set = fetch_func(query=id, t="drama")
    json_dump = json.dumps(data_set, indent=4, sort_keys=True, default=str)

    return json_dump

if __name__ == '__main__':
    app.run(port=7777)
