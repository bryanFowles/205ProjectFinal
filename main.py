from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import requests, json
from pprint import pprint
import pathlib
from pathlib import Path

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# store three foods
foods = [[], [], [], [], [], [], [], [], [],]
endpoint =  'https://www.thecocktaildb.com/api/json/v1/1/filter.php?c=Ordinary_Drink'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}
@app.route('/icecream')
def hello():
    try:
        r = requests.get(endpoint, headers=headers)
        data = r.json()
        for counter, i in enumerate(data['drinks']):
            print(counter)
            foods[counter] = [ i['strDrinkThumb'], i['strDrink']] 
    except:
        print('please try again')
    print(foods)
    return render_template('icecreams.html', foods = foods)

@app.route('/shoppingCart')
def cart():
    return render_template('shopCart.html')

@app.route('/')
def home():
    return render_template('home.html')