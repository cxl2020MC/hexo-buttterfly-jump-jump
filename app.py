from email.errors import FirstHeaderLineIsContinuationDefect
from flask import Flask, request, jsonify, render_template
import random
import yaml
import requests
# import traceback

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.debug = True



@app.route('/', methods=['GET'])
def index():
    data = requests.get('https://github.com/cxl2020MC/cxl2020MC.github.io/raw/master/source/_data/link.yml').text
    jsondata = yaml.load(data)
    print(jsondata)

    friend = []
    for i in jsondata:
        for a in i['link_list']:
            friend.append(a['link'])
    url = friend[random.randint(len(friend)-1)]
    return render_template('tp.html', url = url)

if __name__ == '__main__':
    app.run()
