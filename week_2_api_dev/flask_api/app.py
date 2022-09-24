from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.views import View
from apis.queries.views import api_method
# from apis.queries.endpoints import testview

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# class testview(View):
@app.route('/table')
def get ():
    return api_method()

@app.route('/')
def server_check():
    return "Server is Running",200

    # flask_app.register_blueprint(query_ns)

if __name__ == "__main__":
    app.run(debug = True)

   
