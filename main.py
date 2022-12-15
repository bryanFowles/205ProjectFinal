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

@app.route('/icecream') # Original link was for an ice cream ordering page, but API broke, so we created an ordering Page for cocktails instead.
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

@app.route('/shoppingCart') # Shopping cart for cocktails that the user would like to purchase.
def cart():
    return render_template('shopCart.html')

@app.route('/longIsland')
def longIsland():
    return render_template('longIsland.html')

@app.route('/410gone')
def gone410():
    return render_template('410gone.html')

@app.route('/fifty')
def fifty():
    return render_template('fifty.html')

@app.route('/blue501')
def blue501():
    return render_template('blue501.html')

@app.route('/special69')
def special69():
    return render_template('special69.html')

@app.route('/dayAtTheBeach')
def dayAtTheBeach():
    return render_template('dayAtTheBeach.html')

@app.route('/aFurlong')
def aFurlong():
    return render_template('aFurlong.html')

@app.route('/midsummernight')
def midsummernight():
    return render_template('midsummernight.html')

@app.route('/madalay')
def madalay():
    return render_template('madalay.html')

@app.route('/') # Homepage to introduce the project to users.

def home():
    return render_template('home.html')

""" 
Course: CST 205 (Fall 2022) - Multimedia Design & Programming
Title: Cocktail Ordering
Abstract: We created a webpage starting from a homepage all the way to a shopping cart to allow the user to order cocktails online.
Authors: Bryan Fowles, Elijah Raya, Jared Adams, Maxwelle Tartaglia - Group 3694
Date: December 13, 2022

- Bryan worked on the cart() function, shopCart.html file, created the github repository, and the shopping cart page.
- Elijah and Jared worked on the home() function, home.html, and the shopping cart page.
- Maxwelle worked on the hello() function, icecreams.html file, the cocktail API, and the ordering page.

Github Repository: https://github.com/bryanFowles/205ProjectFinal

"""
