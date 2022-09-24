from flask import Flask, jsonify, request,render_template,make_response
from apis.view import api_method
# creating a Flask app
app = Flask(__name__)

app.route("/table")(api_method)

@app.route('/')
def home():
	return "Server is running",200

if __name__ == '__main__':

	app.run(debug = True)