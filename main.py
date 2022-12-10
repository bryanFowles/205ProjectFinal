from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import requests, json
from pprint import pprint

app = Flask(__name__)
bootstrap = Bootstrap5(app)

endpoint = "https://ig-food-menus.herokuapp.com/ice-cream"

# try:
#   r = requests.get(endpoint)
#   data = r.json()
#   pprint(data)
# except:
#   print('please try again')
icecreamlist = [

]

@app.route('/')
def main():
    try:
        r = requests.get(endpoint)
        data = r.json()
        # print(data)
        for n in data:
            if (n['name'] == "The Baked Bear"):
                icecreamlist.append([n['img'], n['name'], n['price']])
            if (n['name'] == "Mochii"):
                icecreamlist.append([n['img'], n['name'], n['price']])
                # print(icecreamlist)
    except:
        print('please try again')
    return render_template('icecreams.html', icecreamlist=icecreamlist)

