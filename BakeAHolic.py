from flask import Flask
from flask import request
import json
# from flask_cors import CORS

app = Flask(__name__)
# CORS(app)

items = {"Bread" : "50",
		 "Black Forest Cake" : "250"}

items = json.dumps(items)

shoppingCart = {}

@app.route('/v1/items', methods=['GET'])
def funItems():
	if request.method == 'GET':		
		return items

@app.route('/v1/addItem', methods=['POST'])
def addItems():
	if request.method == 'POST':
		shoppingCart[request.form['itemName']] = request.form['number']
		# print(shoppingCart)
		return json.dumps(shoppingCart)

@app.route('/v1/cart', methods=['GET'])
def showCart():
	if request.method == 'GET':		
		return json.dumps(shoppingCart)

if __name__ == '__main__':
	app.run(debug = True)