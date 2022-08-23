from flask import Flask, request, jsonify, render_template
import random
import yaml
import requests
import os
# import traceback

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
app.debug = True



@app.route('/', methods=['GET'])
def index():
    url = os.getenv('URL')
    print(url)
    if url == None:
        return 'URL环境变量未设置'
    yamldata = requests.get(url).text
    print(yamldata)
    data = yaml.load(yamldata)
    print(data)

    friends = []
    for i in data:
        for i in i['link_list']:
            friends.append({'url': i['link'], 'name': i['name']})
    print(friends)
    data = friends[random.randint(0, len(friends)-1)]
    return render_template('tp.html', url = data['url'], name = data['name'])

if __name__ == '__main__':
    app.run()
