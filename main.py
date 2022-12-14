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

"""
